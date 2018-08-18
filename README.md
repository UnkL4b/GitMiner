![Screenshot](https://3.bp.blogspot.com/-UvpR_QDDAT0/VtiIc8OKrrI/AAAAAAAAboM/69BNKrvdUsU/s1600/gitminer-628x360.png)

```
 + Autor: UnK
 + Blog: https://unkl4b.github.io
 + Github: https://github.com/danilovazb
 + Twitter: https://twitter.com/danilo_vaz_
```
## WARNING
```
 +---------------------------------------------------+
 | DEVELOPERS ASSUME NO LIABILITY AND ARE NOT        |
 | RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY    |
 | THIS PROGRAM                                      |
 +---------------------------------------------------+
```

### DESCRIPTION
```
Advanced search tool and automation in Github.
This tool aims to facilitate research by code or code 
snippets on github through the site's search page.
```
### MOTIVATION
Demonstrates the fragility of trust in public repositories to store codes with sensitive information.

### REQUIREMENTS
```
lxml
requests
```

### INSTALL
```
git clone http://github.com/UnkL4b/GitMiner

sudo apt-get install python-requests python-lxml 
OR
pip install -r requirements.txt
```
### Docker
```
git clone http://github.com/UnkL4b/GitMiner
cd GitMiner
docker build -t gitminer .
docker run -it gitminer -h
```


### HELP
```

                                 UnkL4b
  __                   Automatic search for Github
((OO))   ▄████  ██▓▄▄▄█████▓ ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███  
 \__/   ██▒ ▀█▒▓██▒▓  ██▒ ▓▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒      OO
  |^|  ▒██░▄▄▄░▒██▒▒ ▓██░ ▒░▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒      oOo
  | |  ░▓█  ██▓░██░░ ▓██▓ ░ ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄      OoO
  | |  ░▒▓███▀▒░██░  ▒██▒ ░ ▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒  /oOo 
  | |___░▒___▒_░▓____▒_░░___░_▒░___░__░░▓__░_▒░___▒_▒_░░_▒░_░░_▒▓_░▒▓░_/ /
  \______░___░__▒_░____░____░__░______░_▒_░░_░░___░_▒░_░_░__░__░▒_░_▒░__/  v2.0
       ░ ░   ░  ▒ ░  ░      ░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ 
             ░  ░                  ░    ░           ░    ░  ░   ░     

  -> github.com/UnkL4b
  -> unkl4b.github.io

  +---------------------[WARNING]---------------------+
  | DEVELOPERS ASSUME NO LIABILITY AND ARE NOT        |
  | RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY    |
  | THIS PROGRAM                                      |
  +---------------------------------------------------+ 
       [-h] [-q 'filename:shadow path:etc']
       [-m wordpress] [-o result.txt]
       [-r '/^\s*.*?;?\s*$/gm']
       [-c _octo=GH1.1.2098292984896.153133829439; _ga=GA1.2.36424941.153192375318; user_session=oZIxL2_ajeDplJSndfl37ddaLAEsR2l7myXiiI53STrfhqnaN; __Host-user_session_same_site=oXZxv9_ajeDplV0gAEsmyXiiI53STrfhDN; logged_in=yes; dotcom_user=unkl4b; tz=America%2FSao_Paulo; has_recent_activity=1; _gh_sess=MmxxOXBKQ1RId3NOVGpGcG54aEVnT1o0dGhxdGdzWVpySnFRd1dVYUk5TFZpZXFuTWxOdW1FK1IyM0pONjlzQWtZM2xtaFR3ZDdxlGMCsrWnBIdnhUN0tjVUtMYU1GeG5Pbm5DMThuWUFETnZjcllGOUNkRGUwNUtKOVJTaGR5eUJYamhWRE5XRnMWZZN3Y3dlpFNDZXL1NWUEN4c093RFhQd3RJQ1NBdmhrVDE3VVNiUFF3dHBycC9FeDZ3cFVXV0ZBdXZieUY5WDRlOE9ZSG5sNmRHUmllcmk0Up1MTcyTXZrN1RHYmJSdz09--434afdd652b37745f995ab55fc83]

optional arguments:
  -h, --help            show this help message and exit
  -q 'filename:shadow path:etc', --query 'filename:shadow path:etc'
                        Specify search term
  -m wordpress, --module wordpress
                        Specify the search module
  -o result.txt, --output result.txt
                        Specify the output file where it will be
                        saved
  -r '/^\s*(.*?);?\s*$/gm', --regex '/^\s*(.*?);?\s*$/gm'
                        Set regex to search in file
  -c _octo=GH1.1.2098292984896.153133829439; _ga=GA1.2.36424941.153192375318; user_session=oZIxL2_ajeDplJSndfl37ddaLAEsR2l7myXiiI53STrfhqnaN; __Host-user_session_same_site=oXZxv9_ajeDplV0gAEsmyXiiI53STrfhDN; logged_in=yes; dotcom_user=unkl4b; tz=America%2FSao_Paulo; has_recent_activity=1; _gh_sess=MmxxOXBKQ1RId3NOVGpGcG54aEVnT1o0dGhxdGdzWVpySnFRd1dVYUk5TFZpZXFuTWxOdW1FK1IyM0pONjlzQWtZM2xtaFR3ZDdxlGMCsrWnBIdnhUN0tjVUtMYU1GeG5Pbm5DMThuWUFETnZjcllGOUNkRGUwNUtKOVJTaGR5eUJYamhWRE5XRnMWZZN3Y3dlpFNDZXL1NWUEN4c093RFhQd3RJQ1NBdmhrVDE3VVNiUFF3dHBycC9FeDZ3cFVXV0ZBdXZieUY5WDRlOE9ZSG5sNmRHUmllcmk0Up1MTcyTXZrN1RHYmJSdz09--434afdd652b37745f995ab55fc83, --cookie _octo=GH1.1.2098292984896.153133829439; _ga=GA1.2.36424941.153192375318; user_session=oZIxL2_ajeDplJSndfl37ddaLAEsR2l7myXiiI53STrfhqnaN; __Host-user_session_same_site=oXZxv9_ajeDplV0gAEsmyXiiI53STrfhDN; logged_in=yes; dotcom_user=unkl4b; tz=America%2FSao_Paulo; has_recent_activity=1; _gh_sess=MmxxOXBKQ1RId3NOVGpGcG54aEVnT1o0dGhxdGdzWVpySnFRd1dVYUk5TFZpZXFuTWxOdW1FK1IyM0pONjlzQWtZM2xtaFR3ZDdxlGMCsrWnBIdnhUN0tjVUtMYU1GeG5Pbm5DMThuWUFETnZjcllGOUNkRGUwNUtKOVJTaGR5eUJYamhWRE5XRnMWZZN3Y3dlpFNDZXL1NWUEN4c093RFhQd3RJQ1NBdmhrVDE3VVNiUFF3dHBycC9FeDZ3cFVXV0ZBdXZieUY5WDRlOE9ZSG5sNmRHUmllcmk0Up1MTcyTXZrN1RHYmJSdz09--434afdd652b37745f995ab55fc83
                        Specify the cookie for your github

```

### EXAMPLE
Searching for wordpress configuration files with passwords:
```
$:> python gitminer-v2.0.py -q 'filename:wp-config extension:php FTP_HOST in:file ' -m wordpress -c pAAAhPOma9jEsXyLWZ-16RTTsGI8wDawbNs4 -o result.txt
```
![Screenshot](https://2.bp.blogspot.com/-GbpzROiEynQ/VtLytfMqQiI/AAAAAAAAbnk/5hDphP4Mbf4/s1600/wordpressEX.png)

Looking for brasilian government files containing passwords:
```
$:> python gitminer-v2.0.py --query 'extension:php "root" in:file AND "gov.br" in:file' -m senhas -c pAAAhPOma9jEsXyLWZ-16RTTsGI8wDawbNs4
```

Looking for shadow files on the etc paste:
```
$:> python gitminer-v2.0.py --query 'filename:shadow path:etc' -m root -c pAAAhPOma9jEsXyLWZ-16RTTsGI8wDawbNs4
```

Searching for joomla configuration files with passwords:
```
$:> python gitminer-v2.0.py --query 'filename:configuration extension:php "public password" in:file' -m joomla -c pAAAhPOma9jEsXyLWZ-16RTTsGI8wDawbNs4
```
![Screenshot](https://3.bp.blogspot.com/-1AsNmFKfsoA/VtLyvJFy2WI/AAAAAAAAbno/C7xTbxtzOo8/s1600/joomlaEX.png)

### Hacking SSH Servers

[![Hacking SSH Servers](https://img.youtube.com/vi/yIJOlKZwQQw/0.jpg)](https://www.youtube.com/watch?v=yIJOlKZwQQw)
