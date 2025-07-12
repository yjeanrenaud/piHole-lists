# piHole-lists
I collect the addresses of ad-blocking, phishing and telemtry lists here for [Pi-Hole installations](https://github.com/pi-hole).
## adlists.csv
The file [adlists.csv](https://github.com/yjeanrenaud/piHole-lists/blob/main/adlists.csv) contains URLs of ads and telemetry lists, especially for Windows machines, that I tend to block in my networks using [Pi-hole](https://github.com/pi-hole). They sum up to about 2 million domains.
## domainlist.csv
The file [domainlist.csv](https://github.com/yjeanrenaud/piHole-lists/blob/main/domainlist.csv) contains domains that I allowed in Pi-hole.
Most of them are still bad actors that collect arbitrary data about users, but are somehow necessary if you want to keep using a specific service. E.g. Google Play or Windows  Updates. It also contains some single domain entries to block (type 1 and 3), that I found annoying because of their ads, e.g. vidcrunch.
The type column
- 0: Allowed domains
- 1: Blocked domains
- 2: Allowed with wildcards/regex
- 3: Blocked with wildcards/regex
# How to use
You can't import them to your Pi-hole. Its Teleport Feature works differently. Hence, you may open the csv files in the speadsheet app at your discretion. You can even just look at the tables here on GitHub. Then, copy the entries to your Pi-hole configuration. Thi way, you also may double-check if you are happy with these entries.

Feel free to use, adapt or extend these lists. No warranty, liability or claims whatsoever.
