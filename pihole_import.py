#!/usr/bin/env python3
"""
pihole_import.py
A small script to import Pi-hole v6 adlists or manual domain rules from CSV via REST API.
2026, Yves Jeanrenaud
A-GPL 3.0
https://github.com/yjeanrenaud/piHole-lists/
---

Environment variables:
    PIHOLE_URL      e.g. `export PIHOLE_URL='http://192.168.1.10'` (or http://192.168.1.10/api)
    PIHOLE_API_KEY  Pi-hole v6 application password (not a static API token), e.g.  
   ```
   read -rsp "Pi-hole API key: " PIHOLE_API_KEY
   echo
   export PIHOLE_API_KEY
   ```

Usage:
```
    python3 pihole_import.py --ads [adlists.csv]
    python3 pihole_import.py --domains [domains.csv]
    python3 pihole_import.py --ads --dry-run
    python3 pihole_import.py --ads --update-gravity
```
"""

import argparse
import csv
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

DOMAIN_TYPES = {
    "exact_allow": ("allow", "exact"),
    "exact_deny": ("deny", "exact"),
    "regex_allow": ("allow", "regex"),
    "regex_deny": ("deny", "regex"),
    "0": ("allow", "exact"),
    "1": ("deny", "exact"),
    "2": ("allow", "regex"),
    "3": ("deny", "regex"),
}


class ApiError(Exception):
    pass


class PiHole:
    def __init__(self, url, password):
        url = url.rstrip("/")
        if url.endswith("/api"):
            self.base = url
        else:
            self.base = url + "/api"
        if urlsplit(self.base).scheme not in ("http", "https"):
            raise ValueError("PIHOLE_URL must start with http:// or https://")
        self.password = password
        self.sid = None

    def request(self, path, method="GET", data=None, timeout=30):
        headers = {"Accept": "application/json"}
        if self.sid:
            headers["X-FTL-SID"] = self.sid
        if data is not None:
            headers["Content-Type"] = "application/json"

        req = Request(
            self.base + path,
            data=json.dumps(data).encode("utf-8") if data is not None else None,
            headers=headers,
            method=method,
        )
        try:
            with urlopen(req, timeout=timeout) as response:
                body = response.read().decode("utf-8")
                if not body:
                    return {}
                try:
                    return json.loads(body)
                except json.JSONDecodeError:
                    return {"message": body}
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:500]
            raise ApiError(f"HTTP {exc.code}: {detail}") from exc
        except URLError as exc:
            raise ApiError(f"Connection error: {exc.reason}") from exc

    def login(self):
        result = self.request("/auth", "POST", {"password": self.password})
        session = result.get("session", {})
        if not session.get("valid") or not session.get("sid"):
            raise ApiError("Pi-hole authentication failed")
        self.sid = session["sid"]

    def logout(self):
        if self.sid:
            try:
                self.request("/auth", "DELETE")
            except ApiError as exc:
                print(f"Warning: could not log out: {exc}", file=sys.stderr)
            finally:
                self.sid = None



