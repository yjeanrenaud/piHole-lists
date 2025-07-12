# piHole-lists
I collect the addresses of adblocking, phishing and telemtry lists here for [Pi-Hole installations](https://github.com/pi-hole).
## adlists.csv
The file [adlists.csv](https://github.com/yjeanrenaud/piHole-lists/blob/main/adlists.csv) contains URLs of ads and telemetry lists, especially for windows machines, that I tend to block in my networks using [Pi-hole](https://github.com/pi-hole). They sum up to about 2 million domains.
## domainlist.csv
The file [domainlist.csv](https://github.com/yjeanrenaud/piHole-lists/blob/main/domainlist.csv) containts domains that I whitelist in Pi-hole.
Most of them are still bad actors collecting arbitary data about users, but somehow are necessary if you want to keep using a specific service. E.g. google play or Win10 updates. It also contains some single domain entries to block (type=3), that annoyed me with their ads, e.g. vidcrunch.
# How to use
You can't import them to your Pi-hole. Its teleport-Feature works differently. Hense, you open the csv files in the speadsheet app at your discretion (you may even just look at the tables here on github) and copy the entries to your Pi-hole configuration. Like that, you also may double check if you are happy with these entries.

Feel free to use, adapt or extend. No warranty whatsoever.
