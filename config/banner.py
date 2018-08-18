import random

colors = {
    'ITALIC':'\033[3m',
    'BOLD':'\033[1m',
    'RED':'\033[1;91m',
    'BLUE':'\033[1;94m',
    'GREEN':'\033[92m',
    'YELLOW':'\033[1;93m',
    'END':'\033[0m',
    }

banner_1 = """
                        ~> UnkL4b <~
{RED}   ██████╗ ██╗████████╗███╗   ███╗██╗███╗   ██╗███████╗██████╗
  ██╔════╝ ██║╚══██╔══╝████╗ ████║██║████╗  ██║██╔════╝██╔══██╗
  ██║  ███╗██║   ██║   ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝
  ██║   ██║██║   ██║   ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗
  ╚██████╔╝██║   ██║   ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║
   ╚═════╝ ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ {END}v2.0
  -
  Automatic search for GitHub.
 
  + {RED}Blog{END}: unkl4b.github.io
  + {RED}Github{END}: github.com/UnkL4b

  +---------------------[{YELLOW}WARNING{END}]---------------------+
  | DEVELOPERS ASSUME NO LIABILITY AND ARE NOT        |
  | RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY    |
  | THIS PROGRAM                                      |
  +---------------------------------------------------+ """.format(**colors)

banner_2 = """

                                 UnkL4b
  __                   Automatic search for Github
(({RED}OO{END})) {RED}  ▄████  ██▓▄▄▄█████▓ ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███  {END}
 \\__/ {RED}  ██▒ ▀█▒▓██▒▓  ██▒ ▓▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒ {END}     OO
  |^|{RED}  ▒██░▄▄▄░▒██▒▒ ▓██░ ▒░▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒ {END}     oOo
  | |{RED}  ░▓█  ██▓░██░░ ▓██▓ ░ ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  {END}    OoO
  | |{RED}  ░▒▓███▀▒░██░  ▒██▒ ░ ▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒{END}  /oOo 
  | |___{RED}░▒{END}___{RED}▒{END}_{RED}░▓{END}____{RED}▒{END}_{RED}░░{END}___{RED}░{END}_{RED}▒░{END}___{RED}░{END}__{RED}░░▓{END}__{RED}░{END}_{RED}▒░{END}___{RED}▒{END}_{RED}▒{END}_{RED}░░{END}_{RED}▒░{END}_{RED}░░{END}_{RED}▒▓{END}_{RED}░▒▓░{END}_/ /
  \\______{RED}░{END}___{RED}░{END}__{RED}▒{END}_{RED}░{END}____{RED}░{END}____{RED}░{END}__{RED}░{END}______{RED}░{END}_{RED}▒{END}_{RED}░░{END}_{RED}░░{END}___{RED}░{END}_{RED}▒░{END}_{RED}░{END}_{RED}░{END}__{RED}░{END}__{RED}░▒{END}_{RED}░{END}_{RED}▒░{END}__/  v2.0
 {RED}      ░ ░   ░  ▒ ░  ░      ░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ 
             ░  ░                  ░    ░           ░    ░  ░   ░     {END}

  -> github.com/UnkL4b
  -> unkl4b.github.io

  +---------------------[{YELLOW}WARNING{END}]---------------------+
  | DEVELOPERS ASSUME NO LIABILITY AND ARE NOT        |
  | RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY    |
  | THIS PROGRAM                                      |
  +---------------------------------------------------+ """.format(**colors)


banner_3 = """
                        _        {RED}FUCK YOU{END}         _
                       |_|        GITHUB         |_|
                       | |         /^^^\         | |
                      _| |_      (| "o" |)      _| |_
                    _| | | | _    (_---_)    _ | | | |_
                   | | | | |' |    _| |_    | `| | | | |
                   |          |   /     \   |          |
                    \        /  / /(. .)\ \  \        /
                      \    /  / /  | . |  \ \  \    /
                        \  \/ /    ||Y||    \ \/  /
                         \__/      || ||      \__/
                                   () ()
                                   || ||
                                  ooO Ooo          


  + {RED}Blog{END}: unkl4b.github.io
  + {RED}Github{END}: github.com/UnkL4b

  +---------------------[{YELLOW}WARNING{END}]---------------------+
  | DEVELOPERS ASSUME NO LIABILITY AND ARE NOT        |
  | RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY    |
  | THIS PROGRAM                                      |
  +---------------------------------------------------+ 



"""

def banner():
    banners = [banner_1, banner_2]
    return(random.choice(banners))

