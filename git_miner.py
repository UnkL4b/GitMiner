# -*- coding: utf-8 -*-
import requests
import argparse
import json
from lxml import html
import os
import codecs
from RichConsole import groups, Sheet

os.system('cls' if os.name == 'nt' else 'clear')
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class frescurinha:
    HELP = groups.Fore.lightcyanEx
    OKBLUE = groups.Fore.lightblueEx
    OKGREEN = groups.Fore.lightgreenEx
    WARNING = Sheet((groups.Brightness.bright, groups.Fore.lightyellowEx))
    FAIL = Sheet((groups.Brightness.bright, groups.Fore.lightredEx))
    ENDC = '\033[0m'

class GitMiner(object):

    def __init__(self):

        self.descricao = frescurinha.OKGREEN("""
 ██████╗ ██╗████████╗███╗   ███╗██╗███╗   ██╗███████╗██████╗
██╔════╝ ██║╚══██╔══╝████╗ ████║██║████╗  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║   ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝
██║   ██║██║   ██║   ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╔╝██║   ██║   ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║
 ╚═════╝ ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ v1.1
 Automatic search for GitHub.

 """)+frescurinha.FAIL("""+ Autor:""")+""" Danilo Vaz a.k.a. UNK
 """+frescurinha.FAIL("""+ Blog:""")+""" http://unk-br.blogspot.com
 """+frescurinha.FAIL("""+ Github:""")+""" http://github.com/danilovazb
 """+frescurinha.FAIL("""+ Gr33tz:""")+""" l33t0s, RTFM
""" + frescurinha.WARNING( \
"\n +[" + frescurinha.FAIL("WARNING") + \
"]------------------------------------------+" \
"\n | DEVELOPERS ASSUME NO LIABILITY AND ARE NOT        |" \
"\n | RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY    |" \
"\n | THIS PROGRAM                                      |" \
"\n +---------------------------------------------------+\n\n"

        parser = argparse.ArgumentParser(self.descricao)
        parser.add_argument('-q','--query', metavar=frescurinha.OKBLUE('\'filename:shadow path:etc\'')\
            , help=frescurinha.HELP('Specify search term')
        parser.add_argument('-m','--module', metavar=frescurinha.OKBLUE('wordpress'),\
            help=frescurinha.HELP('Specify the search module', default=None)
        parser.add_argument('-o','--output', metavar=frescurinha.OKBLUE('result.txt'),\
            help=frescurinha.HELP('Specify the output file where it will be saved'),default=None)
        parser.add_argument('-c','--cookie', metavar=frescurinha.OKBLUE('pAAAhPOma9jEsXyLWZ-16RTTsGI8wDawbNs4'),\
            help=frescurinha.HELP('Specify the cookie for your github'),default=None)

        self.url = "http://github.com"
        self.user_agent = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}
        self.args = parser.parse_args()
        self.cookie = {'user_session':self.args.cookie}
        if self.args.query is None:
            os.system('cls' if os.name == 'nt' else 'clear')
            parser.print_help()
            exit()
        self.search_term = "/search?o=desc&q=%s&s=indexed&type=Code&utf8=✓" % self.args.query
        self.ignora_modulo = "n"
        self.config = None
        self.number_page = None

    def saveOutput(self,text):
        if self.args.output is not None:
            arquivo = open(self.args.output, 'a')
            arquivo.write(text.encode("utf-8"))
            arquivo.close()

    def nextPage(self,prox_page):
        print(frescurinha.HELP("\n+[PAGE %s/%s]-----------------------------------------+" % (prox_page.split("&")[1].split("=")[1], self.number_page))
        self.saveOutput("\n+[PAGE %s/%s]-----------------------------------------+\n" % (prox_page.split("&")[1].split("=")[1], self.number_page))
        HTML = self.accessWeb(prox_page)
        self.parseSearch(HTML.content)

    def carregaConf(self):
        if "n" in self.ignora_modulo:
            with open("config/parsers.json",'r') as arq_config:
                confs = arq_config.read()
            try:
                confs_json = json.loads(confs)

            except:
                print(frescurinha.FAIL("\n[!] Configuration file not found in \"configs/\"" \
                    "or not set.\nYou want to abort? [Y] [N]"))
                resp = raw_input()
                if "y" in resp.lower():
                    exit()
                elif "n" in resp.lower():
                    self.ignora_modulo = "s"
            try:
                if self.args.module not in confs_json.keys():
                    print(frescurinha.WARNING("\n[?] \"%s\" module not set\nYou want to abort? [Y] [N] \n" % self.args.module))
                    resp = raw_input()
                    if "y" in resp.lower():
                        exit()
                    elif "n" in resp.lower():
                        self.ignora_modulo = "s"

                elif self.args.module in confs_json.keys():
                    return confs_json

                elif "s" in self.ignora_modulo:
                    pass

            except UnboundLocalError:
                pass

        elif "s" in self.ignora_modulo:
            pass

    def parseCode(self, code_boladao):
        result_code = []
        if self.config is None:
            pass
        else:
            if "" == self.config[self.args.module]['contains']:
                pass
            else:
                for line in range(len(code_boladao.split("\n"))):
                    if self.config[self.args.module]['contains'] in code_boladao.split("\n")[int(line)-1]:
                        print("| [" + frescurinha.OKBLUE("CONTAIN") + "]: \"%s\" IN LINE: %s" % (self.config[self.args.module]['contains'], str(line)))
                        self.saveOutput("| [CONTAIN]: \"%s\" IN LINE: %s\n" % (self.config[self.args.module]['contains'], str(line)))

            if not self.config[self.args.module]['parameters']:
                print(frescurinha.HELP("+----------------------------------------------------+"))
                self.saveOutput("+----------------------------------------------------+\n")

            if self.config[self.args.module]['parameters'] >= 1:
                qtd_param = int(len(self.config[self.args.module]['parameters']))
                qtd_order = int(len(self.config[self.args.module]['splitorder']))
                split_param = self.config[self.args.module]['splitparam']
                for qtd in range(qtd_param):
                    param_name = "param%s" % str(qtd+1)
                    for line in range(len(code_boladao.split("\n"))):
                        if self.config[self.args.module]['parameters'][param_name] in code_boladao.split("\n")[int(line)-1]:
                            line_code = code_boladao.split("\n")[int(line)-1]
                            if qtd_order == 0:
                                result_code.append(line_code)
                            for o_qtd in range(qtd_order):
                                order_name = "order%s" % str(o_qtd+1)
                                try:
                                    result_code.append(line_code.split("%s" % split_param)[int(self.config[self.args.module]['splitorder'][order_name])])
                                except IndexError:
                                    pass
                                #print(line_code.split("%s" % split_param)[int(self.config[self.args.module]['splitorder'][order_name])])

            else:
                print(frescurinha.HELP("+----------------------------------------------------+"))
                self.saveOutput("+----------------------------------------------------+\n")
                pass

        if result_code:
            print("| [" + frescurinha.OKBLUE("PARAM FOUND") + "]:")
            self.saveOutput("| [PARAM FOUND]:\n")
            for i in range(len(result_code)):
                print("|" + frescurinha.WARNING(" -------------> ") + "%s" % result_code[i])
                self.saveOutput("| -------------> %s\n" % result_code[i])
            print(frescurinha.HELP("+----------------------------------------------------+"))
            self.saveOutput("+----------------------------------------------------+\n")

    def parseSearch(self,response):
        tree = html.fromstring(response)
        url_arquivo = tree.xpath('//div[contains(@class, "code-list-item-public")]/div[contains(@class, "d-inline-block")]/a[2]/@href')
        last_indexed = tree.xpath('//div[contains(@class, "code-list-item-public")]/div[contains(@class, "mb-2")]/span[2]/relative-time/@title')
        usuario = tree.xpath('//div[contains(@class, "code-list-item-public")]/a/img/@alt')
        prox_page = tree.xpath('//a[contains(@class, "next_page")]/@href')
        for number_link in range(len(url_arquivo)):
            link = self.url + url_arquivo[number_link].replace("blob","raw")
            HTML = self.accessWeb(link)
            code_boladao = HTML.text
            print("| [" + frescurinha.OKBLUE("USER") + "]: %s" % usuario[number_link])
            self.saveOutput("| [USER]: %s\n" % usuario[number_link])
            print("| [" + frescurinha.OKBLUE("LINK") + "]: %s" % link)
            self.saveOutput("| [LINK]: %s\n" % link)
            try:
                print("| [" + frescurinha.OKBLUE("LAST INDEXED") + "]: %s" % last_indexed[number_link])
                self.saveOutput("| [LAST INDEXED]: %s\n" % last_indexed[number_link])
            except:
                pass
            self.parseCode(code_boladao)
            if "s" in self.ignora_modulo:
                print(frescurinha.HELP("+----------------------------------------------------+"))
                self.saveOutput("+----------------------------------------------------+\n")


            #DEBUG DE MLK ZIKA
            #tree_file = html.fromstring(HTML.content)
            #print(tree_file.xpath('//div[contains(@class, "btn-group")]/a[contains(@id, "raw-url")]/@href'))
            #print(frescurinha.OKBLUE("%s" % link))
            #print("%s\n" % HTML.text)

        if not prox_page:
            exit()
        prox_page = prox_page[0]
        prox_page = self.url + prox_page
        self.nextPage(prox_page)

    def accessWeb(self,url_acesso):
        acc = requests.get(url_acesso, headers=self.user_agent, cookies=self.cookie)
        if " find any code matching" in acc.text:
            print(frescurinha.FAIL("[-] We couldn't find any code matching %s\n" % self.args.query))
            exit()
        return acc

    def parserPages(self,response):
        tree = html.fromstring(response)
        number_page = tree.xpath('//div[contains(@class, "pagination")]/a/text()')
        if number_page:
            return number_page[len(number_page)-2]
        else:
            return "1"

    def start(self):
        print(self.descricao)
        self.config = self.carregaConf()
        #print confs_json
        url_acesso = self.url + self.search_term
        HTML = self.accessWeb(url_acesso)
        self.number_page = self.parserPages(HTML.content)
        print(frescurinha.HELP("+[PAGE: 1/%s]-----------------------------------------+" % self.number_page) )
        self.saveOutput("+[PAGE: 1/%s]-----------------------------------------+\n" % self.number_page)
        self.parseSearch(HTML.content)

try:
    GitMiner().start()
except KeyboardInterrupt:
    print(frescurinha.WARNING("\n\nBye Bye ;)") )
    exit()
