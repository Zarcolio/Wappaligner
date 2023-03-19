#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import urllib.parse
from termcolor import colored

try:
    json_data = json.load(sys.stdin)
except json.JSONDecodeError:
    print("Error: Invalid JSON input.")
    sys.exit(1)
except Exception as e:
    print("Error:", e)
    sys.exit(1)

if "urls" not in json_data or "applications" not in json_data:
    print("Error: Invalid input format.")
    sys.exit(1)

for sUrl, data in json_data["urls"].items():
    status = data.get("status", "unknown")
    print(colored(f"URL = {sUrl} (HTTP status {status})", "green"))

for app in json_data["applications"]:
    name = app["name"]
    version = app.get("version", "")
    confidence = app["confidence"]
    sVersion1 = f" {version}" if version else ""
    sVersion2 = f" \"{version}\"" if version else ""
    
    sExploitdbUrl = f"https://www.exploit-db.com/search?q={urllib.parse.quote(name)}"
    sinfosecmatterUrl = f"https://www.google.com/search?q=site%3Ainfosecmatter.com+%22Public+Exploits%22+{urllib.parse.quote(f'"{name}"')}"
    sTenableUrl = f"https://www.google.com/search?q=site%3Atenable.com/plugins+{urllib.parse.quote(f'"{name}"')}"
    sGoogleUrl = f"https://www.google.com/search?q={urllib.parse.quote(f'"{name}"{sVersion2} cve |exploit |vulnerability |update |changelog |risk |advisory |cvss')}"
    
    print(f"{name}{sVersion1} ({confidence}%)")
    print(f" - {app['website']}")
    print(f" - {sExploitdbUrl}")
    print(f" - {sTenableUrl}")
    print(f" - {sinfosecmatterUrl}")
    print(f" - {sGoogleUrl}")
