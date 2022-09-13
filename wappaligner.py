#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys
import urllib.parse
from termcolor import colored

sStandardInput = ""

for x in sys.stdin:
    sStandardInput = sStandardInput + x 

#print (sStandardInput)
try:
    json_data = json.loads(sStandardInput)
except:
    pass

   
for sUrl in json_data["urls"]:
    print (colored("URL = " + sUrl + " (HTTP status "+ str(json_data['urls'][sUrl]['status']) + ")","green"))
#    print (colored("URL = " + sUrl["status"],"green"))

for app in json_data["applications"]:
    if app["version"]:
        sVersion1 = " " + str(app["version"])
        sVersion2 = " \"" + str(app["version"]) + "\""  
    else:
        sVersion1 = ""
        sVersion2 = ""

    sExploitdbUrl = "https://www.exploit-db.com/search?q=" + urllib.parse.quote(app["name"])
    sinfosecmatterUrl = "https://www.google.com/search?q=site%3Ainfosecmatter.com+%22Public+Exploits%22+" + urllib.parse.quote("\"" + app["name"]+ "\"")
    sGoogleUrl = "https://www.google.com/search?q=" + urllib.parse.quote("\"" + app["name"] + "\"" + sVersion2 + " cve |exploit |vulnerability |update |changelog |risk |advisory |cvss")
    print (app["name"] + sVersion1 + " (" + app["confidence"] + "%)")
    print (" - " + app["website"])
    print (" - " + sExploitdbUrl)
    print (" - " + sinfosecmatterUrl)
    print (" - " + sGoogleUrl)
    
