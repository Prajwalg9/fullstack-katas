"""
From : log.txt
192.168.0.10 - - [23/Nov/2025:10:12:01 +0530] "GET /index.html HTTP/1.1" 200 5321
10.0.0.5 - - [23/Nov/2025:10:12:05 +0530] "POST /login HTTP/1.1" 302 1024
192.168.0.10 - - [23/Nov/2025:10:12:10 +0530] "GET /dashboard HTTP/1.1" 200 8450
172.16.0.3 - - [23/Nov/2025:10:12:18 +0530] "GET /assets/style.css HTTP/1.1" 200 2048

Extract all unique IP addresses.
Extract all requested paths (/index.html, /login, /dashboard, /assets/style.css).
Extract all status codes (200, 302, …).
"""

import re
from re import findall

with open("log.txt", "rt") as f:
    data = f.read()

Ip_pattern=r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}"
Url_pattern=r"[/][a-z]+[.]?[/]*[a-z]*[.]?[a-z]+"
statusC_pattern=r"\s\d{1,3}\s"

Ip=re.findall(Ip_pattern,data)
Url=re.findall(Url_pattern,data)
status_codes=re.findall(statusC_pattern,data)

print(f"Ip addresses: {Ip}\nUrl addresses: {Url}\nStatus codes: {set(status_codes)}")