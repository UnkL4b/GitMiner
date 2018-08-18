# -*- coding: utf-8 -*-
import os
import json
import codecs
import requests
import argparse
from config import banner as bn
from config import headers 
from config.banner import colors
from core.loadModule import loadModule
from core.Parser import Parser
from core.sendRequest import requestPage
from core.sendRequest import nextPage

os.system('cls' if os.name == 'nt' else 'clear')
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3

class GitMiner(object):

    def __init__(self):
        self.descricao = bn.banner()
        parser = argparse.ArgumentParser(self.descricao)
        parser.add_argument('-q','--query', metavar='{BLUE}\'filename:shadow path:etc\'{END}'.format(**colors), help='{YELLOW}Specify search term{END}'.format(**colors))
        parser.add_argument('-m','--module', metavar='{BLUE}wordpress{END}'.format(**colors), help='{YELLOW}Specify the search module{END}'.format(**colors), default=None)
        parser.add_argument('-o','--output', metavar='{BLUE}result.txt{END}'.format(**colors), help='{YELLOW}Specify the output file where it will be saved{END}'.format(**colors), default=None)
        parser.add_argument('-r', '--regex', metavar='{BLUE}\'/^\s*(.*?);?\s*$/gm\'{END}'.format(**colors), help='{YELLOW}Set regex to search in file{END}'.format(**colors), default=None)
        parser.add_argument('-c','--cookie', metavar='{BLUE}_octo=GH1.1.2098292984896.153133829439; _ga=GA1.2.36424941.153192375318; user_session=oZIxL2_ajeDplJSndfl37ddaLAEsR2l7myXiiI53STrfhqnaN; __Host-user_session_same_site=oXZxv9_ajeDplV0gAEsmyXiiI53STrfhDN; logged_in=yes; dotcom_user=unkl4b; tz=America%2FSao_Paulo; has_recent_activity=1; _gh_sess=MmxxOXBKQ1RId3NOVGpGcG54aEVnT1o0dGhxdGdzWVpySnFRd1dVYUk5TFZpZXFuTWxOdW1FK1IyM0pONjlzQWtZM2xtaFR3ZDdxlGMCsrWnBIdnhUN0tjVUtMYU1GeG5Pbm5DMThuWUFETnZjcllGOUNkRGUwNUtKOVJTaGR5eUJYamhWRE5XRnMWZZN3Y3dlpFNDZXL1NWUEN4c093RFhQd3RJQ1NBdmhrVDE3VVNiUFF3dHBycC9FeDZ3cFVXV0ZBdXZieUY5WDRlOE9ZSG5sNmRHUmllcmk0Up1MTcyTXZrN1RHYmJSdz09--434afdd652b37745f995ab55fc83{END}'.format(**colors), help='{YELLOW}Specify the cookie for your github{END}'.format(**colors), default=None)
        self.url = "https://github.com"
        self.args = parser.parse_args()
        if self.args.query is None or self.args.cookie is None:
            os.system('cls' if os.name == 'nt' else 'clear')
            parser.print_help()
            exit()
        self.cookie = headers.parseCookie(self.args.cookie)
        self.search_term = "/search?o=desc&q=%s&s=indexed&type=Code" % self.args.query
        self.config = None
        self.number_page = None

    def start(self):
        p = Parser()
        print(self.descricao)
        self.config = loadModule(self.args.module)
        filename = self.args.output
        url_search = self.url + self.search_term
        headers_github = headers.getHeaders(url_search)
        #print(headers_github)
        content_html = requestPage(url_search, headers_github, self.cookie)
        self.number_page = p.getNumPages(content_html.content)
        print("{YELLOW}+[PAGE: 1/%s]▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{END}".format(**colors) \
              % self.number_page)
        if filename is not None:
            write_file = open(filename, 'a')
            write_file.write("[\n")
            write_file.close()
        p.getSearch(content_html.content, self.number_page, headers_github, self.cookie, self.config, filename, self.args.regex)
        if filename is not None:
            write_file = open(filename, 'a')
            write_file.write("\n]")
            write_file.close()

try:
    GitMiner().start()
except KeyboardInterrupt:
    print("{RED}\n\nBye Bye ;){END}".format(**colors))
    exit()
