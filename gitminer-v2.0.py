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
        parser.add_argument('-l','--list', help='{YELLOW}List modules{END}'.format(**colors), action='store_true')
        parser.add_argument('-o','--output', metavar='{BLUE}result.txt{END}'.format(**colors), help='{YELLOW}Specify the output file where it will be saved{END}'.format(**colors), default=None)
        parser.add_argument('-r', '--regex', metavar='{BLUE}\'/^\s*(.*?);?\s*$/gm\'{END}'.format(**colors), help='{YELLOW}Set regex to search in file{END}'.format(**colors), default=None)
        parser.add_argument('-c','--cookie', metavar='{BLUE}cookie.txt{END}'.format(**colors), default=None)
        self.url = "https://github.com"
        self.args = parser.parse_args()
        if self.args.list is True:
            loadModule(self.args.module)
        if self.args.query is None or self.args.cookie is None:
            os.system('cls' if os.name == 'nt' else 'clear')
            parser.print_help()
            exit()
        with open(self.args.cookie) as txt:
            for line in txt:
                self.cookie = headers.parseCookie(line)
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
