[![Python 2.7|3.6](https://img.shields.io/badge/Python-2.7%7C3.6-blue.svg)](https://www.python.org/) [![Gitminer 2.0](https://img.shields.io/badge/Gitminer-2.0-yellow.svg)](https://unkl4b.github.io)

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
argparse
json
re
```

### INSTALL
```
$ git clone http://github.com/UnkL4b/GitMiner

$ cd GitMiner

~/GitMiner $ pip3 install -r requirements.txt
```
### Docker
```
$ git clone http://github.com/UnkL4b/GitMiner
$ cd GitMiner
$ docker build -t gitminer .
$ docker run -it gitminer -h
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
$:> python3 gitminer-v2.0.py -q 'filename:wp-config extension:php FTP_HOST in:file ' -m wordpress -c pAAAhPOma9jEsXyLWZ-16RTTsGI8wDawbNs4 -o result.txt
```
![Screenshot](https://2.bp.blogspot.com/-GbpzROiEynQ/VtLytfMqQiI/AAAAAAAAbnk/5hDphP4Mbf4/s1600/wordpressEX.png)

Looking for brasilian government files containing passwords:
```
$:> python3 gitminer-v2.0.py --query 'extension:php "root" in:file AND "gov.br" in:file' -m senhas -c pAAAhPOma9jEsXyLWZ-16RTTsGI8wDawbNs4
```

Looking for shadow files on the etc paste:
```
$:> python3 gitminer-v2.0.py --query 'filename:shadow path:etc' -m root -c pAAAhPOma9jEsXyLWZ-16RTTsGI8wDawbNs4
```

Searching for joomla configuration files with passwords:
```
$:> python3 gitminer-v2.0.py --query 'filename:configuration extension:php "public password" in:file' -m joomla -c pAAAhPOma9jEsXyLWZ-16RTTsGI8wDawbNs4
```
![Screenshot](https://3.bp.blogspot.com/-1AsNmFKfsoA/VtLyvJFy2WI/AAAAAAAAbno/C7xTbxtzOo8/s1600/joomlaEX.png)

### Hacking SSH Servers

[![Hacking SSH Servers](https://img.youtube.com/vi/yIJOlKZwQQw/0.jpg)](https://www.youtube.com/watch?v=yIJOlKZwQQw)

### Dork to search
##### by @techgaun (https://github.com/techgaun/github-dorks)

 Dork                                           | Description
------------------------------------------------|--------------------------------------------------------------------------
filename:.npmrc _auth                           | npm registry authentication data
filename:.dockercfg auth                        | docker registry authentication data
extension:pem private                           | private keys
extension:ppk private                           | puttygen private keys
filename:id_rsa or filename:id_dsa              | private ssh keys
extension:sql mysql dump                        | mysql dump
extension:sql mysql dump password               | mysql dump look for password; you can try varieties
filename:credentials aws_access_key_id          | might return false negatives with dummy values
filename:.s3cfg                                 | might return false negatives with dummy values
filename:wp-config.php                          | wordpress config files
filename:.htpasswd                              | htpasswd files
filename:.env DB_USERNAME NOT homestead         | laravel .env (CI, various ruby based frameworks too)
filename:.env MAIL_HOST=smtp.gmail.com          | gmail smtp configuration (try different smtp services too)
filename:.git-credentials                       | git credentials store, add NOT username for more valid results
PT_TOKEN language:bash                          | pivotaltracker tokens
filename:.bashrc password                       | search for passwords, etc. in .bashrc (try with .bash_profile too)
filename:.bashrc mailchimp                      | variation of above (try more variations)
filename:.bash_profile aws                      | aws access and secret keys
rds.amazonaws.com password                      | Amazon RDS possible credentials
extension:json api.forecast.io                  | try variations, find api keys/secrets
extension:json mongolab.com                     | mongolab credentials in json configs
extension:yaml mongolab.com                     | mongolab credentials in yaml configs (try with yml)
jsforce extension:js conn.login                 | possible salesforce credentials in nodejs projects
SF_USERNAME salesforce                          | possible salesforce credentials
filename:.tugboat NOT _tugboat                  | Digital Ocean tugboat config
HEROKU_API_KEY language:shell                   | Heroku api keys
HEROKU_API_KEY language:json                    | Heroku api keys in json files
filename:.netrc password                        | netrc that possibly holds sensitive credentials
filename:_netrc password                        | netrc that possibly holds sensitive credentials
filename:hub oauth_token                        | hub config that stores github tokens
filename:robomongo.json                         | mongodb credentials file used by robomongo
filename:filezilla.xml Pass                     | filezilla config file with possible user/pass to ftp
filename:recentservers.xml Pass                 | filezilla config file with possible user/pass to ftp
filename:config.json auths                      | docker registry authentication data
filename:idea14.key                             | IntelliJ Idea 14 key, try variations for other versions
filename:config irc_pass                        | possible IRC config
filename:connections.xml                        | possible db connections configuration, try variations to be specific
filename:express.conf path:.openshift           | openshift config, only email and server thou
filename:.pgpass                                | PostgreSQL file which can contain passwords
filename:proftpdpasswd                          | Usernames and passwords of proftpd created by cpanel
filename:ventrilo_srv.ini                       | Ventrilo configuration
[WFClient] Password= extension:ica              | WinFrame-Client infos needed by users to connect toCitrix Application Servers
filename:server.cfg rcon password               | Counter Strike RCON Passwords
JEKYLL_GITHUB_TOKEN                             | Github tokens used for jekyll
filename:.bash_history                          | Bash history file
filename:.cshrc                                 | RC file for csh shell
filename:.history                               | history file (often used by many tools)
filename:.sh_history                            | korn shell history
filename:sshd_config                            | OpenSSH server config
filename:dhcpd.conf                             | DHCP service config
filename:prod.exs NOT prod.secret.exs           | Phoenix prod configuration file
filename:prod.secret.exs                        | Phoenix prod secret
filename:configuration.php JConfig password     | Joomla configuration file
filename:config.php dbpasswd                    | PHP application database password (e.g., phpBB forum software)
path:sites databases password                   | Drupal website database credentials
shodan_api_key language:python                  | Shodan API keys (try other languages too)
filename:shadow path:etc                        | Contains encrypted passwords and account information of new unix systems
filename:passwd path:etc                        | Contains user account information including encrypted passwords of traditional unix systems
extension:avastlic "support.avast.com"          | Contains license keys for Avast! Antivirus
filename:dbeaver-data-sources.xml               | DBeaver config containing MySQL Credentials
filename:.esmtprc password                      | esmtp configuration
extension:json googleusercontent client_secret  | OAuth credentials for accessing Google APIs
HOMEBREW_GITHUB_API_TOKEN language:shell        | Github token usually set by homebrew users
xoxp OR xoxb                                    | Slack bot and private tokens
.mlab.com password                              | MLAB Hosted MongoDB Credentials
filename:logins.json                            | Firefox saved password collection (key3.db usually in same repo)
filename:CCCam.cfg                              | CCCam Server config file
msg nickserv identify filename:config           | Possible IRC login passwords
filename:settings.py SECRET_KEY                 | Django secret keys (usually allows for session hijacking, RCE, etc)
filename:secrets.yml password                   | Usernames/passwords, Rails applications
filename:master.key path:config                 | Rails master key (used for decrypting `credentials.yml.enc` for Rails 5.2+)
filename:deployment-config.json                 | Created by sftp-deployment for Atom, contains server details and credentials
filename:.ftpconfig                             | Created by remote-ssh for Atom, contains SFTP/SSH server details and credentials
filename:.remote-sync.json                      | Created by remote-sync for Atom, contains FTP and/or SCP/SFTP/SSH server details and credentials
filename:sftp.json path:.vscode                 | Created by vscode-sftp for VSCode, contains SFTP/SSH server details and credentails
filename:sftp-config.json                       | Created by SFTP for Sublime Text, contains FTP/FTPS or SFTP/SSH server details and credentials
filename:WebServers.xml                         | Created by Jetbrains IDEs, contains webserver credentials with encoded passwords ([not encrypted!](https://intellij-support.jetbrains.com/hc/en-us/community/posts/207074025/comments/207034775))
