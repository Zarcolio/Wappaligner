# Wappaligner

"*Wappalyzer is a cross-platform utility that uncovers the technologies used on websites. It detects content management systems, ecommerce platforms, web frameworks, server software, analytics tools and many more.*"

Wappaligner changes the output of Wappalyzer into something human readable. It also provides links to useful websites and a Google query for finding information on vulnerabilities.
No installation is needed.

# Install Wappalyzer
`wappalyzer-installer.sh`

# Use Wappaligner
`wappalyzer http://scanme.nmap.org | wappaligner`

This returns:
URL = http://scanme.nmap.org/ (HTTP status 200)

Apache 2.4.7 (100%)
 - http://apache.org
 - https://www.exploit-db.com/search?q=Apache
 - https://www.google.com/search?q=site%3Ainfosecmatter.com+%22Public+Exploits%22+%22Apache%22
 - https://www.google.com/search?q=%22Apache%22%20%222.4.7%22%20cve%20%7Cexploit%20%7Cvulnerability%20%7Cupdate%20%7Cchangelog%20%7Crisk%20%7Cadvisory%20%7Ccvss
 
Google Analytics (100%)
 - http://google.com/analytics
 - https://www.exploit-db.com/search?q=Google%20Analytics
 - https://www.google.com/search?q=site%3Ainfosecmatter.com+%22Public+Exploits%22+%22Google%20Analytics%22
 - https://www.google.com/search?q=%22Google%20Analytics%22%20cve%20%7Cexploit%20%7Cvulnerability%20%7Cupdate%20%7Cchangelog%20%7Crisk%20%7Cadvisory%20%7Ccvss
 
Ubuntu (100%)
 - http://www.ubuntu.com/server
 - https://www.exploit-db.com/search?q=Ubuntu
 - https://www.google.com/search?q=site%3Ainfosecmatter.com+%22Public+Exploits%22+%22Ubuntu%22
 - https://www.google.com/search?q=%22Ubuntu%22%20cve%20%7Cexploit%20%7Cvulnerability%20%7Cupdate%20%7Cchangelog%20%7Crisk%20%7Cadvisory%20%7Ccvss
