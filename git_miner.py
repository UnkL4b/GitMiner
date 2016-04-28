# -*- coding: utf-8 -*-
import requests
import argparse
import json
from lxml import html
import os
import codecs

os.system('cls' if os.name == 'nt' else 'clear')
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

class frescurinha:
    HELP = '\033[1;36m'
    OKBLUE = '\033[1;94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[1;93m'
    FAIL = '\033[1;91m'
    ENDC = '\033[0m'

class GitMiner(object):

    def __init__(self):

        self.descricao = frescurinha.OKGREEN+"""
 ██████╗ ██╗████████╗███╗   ███╗██╗███╗   ██╗███████╗██████╗
██╔════╝ ██║╚══██╔══╝████╗ ████║██║████╗  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║   ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝
██║   ██║██║   ██║   ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╔╝██║   ██║   ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║
 ╚═════╝ ╚═╝   ╚═╝   ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ v1.1
 Automatic search for GitHub.

 """+frescurinha.ENDC+frescurinha.FAIL+"""+ Autor:"""+frescurinha.ENDC+""" Danilo Vaz a.k.a. UNK
 """+frescurinha.FAIL+"""+ Blog:"""+frescurinha.ENDC+""" http://unk-br.blogspot.com
 """+frescurinha.FAIL+"""+ Github:"""+frescurinha.ENDC+""" http://github.com/danilovazb
 """+frescurinha.FAIL+"""+ Gr33tz:"""+frescurinha.ENDC+""" l33t0s, RTFM
""" + frescurinha.WARNING + \
"\n +[" + frescurinha.FAIL + "WARNING" + frescurinha.WARNING \
+ "]------------------------------------------+" \
"\n | DEVELOPERS ASSUME NO LIABILITY AND ARE NOT        |" \
"\n | RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY    |" \
"\n | THIS PROGRAM                                      |" \
"\n +---------------------------------------------------+\n\n" + frescurinha.ENDC

        parser = argparse.ArgumentParser(self.descricao)
        parser.add_argument('-q','--query', metavar=frescurinha.OKBLUE + '\'filename:shadow path:etc\''\
            + frescurinha.ENDC, help=frescurinha.HELP + 'Specify search term' + frescurinha.ENDC)
        parser.add_argument('-m','--module', metavar=frescurinha.OKBLUE + 'wordpress' + frescurinha.ENDC,\
            help=frescurinha.HELP + 'Specify the search module' + frescurinha.ENDC, default=None)
        parser.add_argument('-o','--output', metavar=frescurinha.OKBLUE + 'result.txt' + frescurinha.ENDC,\
            help=frescurinha.HELP + 'Specify the output file where it will be saved' + frescurinha.ENDC,default=None)

        self.url = "http://github.com"
        self.user_agent = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36"}
        self.args = parser.parse_args()
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
        print(frescurinha.HELP + "\n+[PAGE %s/%s]-----------------------------------------+" % (prox_page.split("&")[1].split("=")[1], self.number_page) + frescurinha.ENDC)
        self.saveOutput("\n+[PAGE %s/%s]-----------------------------------------+\n" % (prox_page.split("&")[1].split("=")[1], self.number_page) + frescurinha.ENDC)
        HTML = self.accessWeb(prox_page)
        self.parseSearch(HTML.content)

    def carregaConf(self):
        if "n" in self.ignora_modulo:
            with open("config/parsers.json",'r') as arq_config:
                confs = arq_config.read()
            try:
                confs_json = json.loads(confs)

            except:
                print(frescurinha.FAIL + "\n[!] Configuration file not found in \"configs/\"" \
                    "or not set.\nYou want to abort? [Y] [N]" + frescurinha.ENDC)
                resp = raw_input()
                if "y" in resp.lower():
                    exit()
                elif "n" in resp.lower():
                    self.ignora_modulo = "s"
            try:
                if self.args.module not in confs_json.keys():
                    print(frescurinha.WARNING + "\n[?] \"%s\" module not set\nYou want to abort? [Y] [N] \n" % self.args.module + frescurinha.ENDC)
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
                        print("| [" + frescurinha.OKBLUE + "CONTAIN" + frescurinha.ENDC + "]: \"%s\" IN LINE: %s" % (self.config[self.args.module]['contains'], str(line)))
                        self.saveOutput("| [CONTAIN]: \"%s\" IN LINE: %s\n" % (self.config[self.args.module]['contains'], str(line)))

            if not self.config[self.args.module]['parameters']:
                print(frescurinha.HELP + "+----------------------------------------------------+"+ frescurinha.ENDC)
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
                print(frescurinha.HELP + "+----------------------------------------------------+"+ frescurinha.ENDC)
                self.saveOutput("+----------------------------------------------------+\n")
                pass

        if result_code:
            print("| [" + frescurinha.OKBLUE + "PARAM FOUND" + frescurinha.ENDC + "]:")
            self.saveOutput("| [PARAM FOUND]:\n")
            for i in range(len(result_code)):
                print("|" + frescurinha.WARNING + " -------------> " + frescurinha.ENDC + "%s" % result_code[i])
                self.saveOutput("| -------------> %s\n" % result_code[i])
            print(frescurinha.HELP + "+----------------------------------------------------+"+ frescurinha.ENDC)
            self.saveOutput("+----------------------------------------------------+\n")

    def parseSearch(self,response):
        tree = html.fromstring(response)
        url_arquivo = tree.xpath('//div[contains(@class, "code-list-item-public")]/p[contains(@class, "title")]/a[2]/@href')
        last_indexed = tree.xpath('//div[contains(@class, "code-list-item-public")]/p[contains(@class, "title")]\
                                  /span[contains(@class, "updated-at")]/time/text()')
        usuario = tree.xpath('//div[contains(@class, "code-list-item-public")]/a/img[contains(@class, "avatar")]/@alt')
        prox_page = tree.xpath('//a[contains(@class, "next_page")]/@href')
        for number_link in range(len(url_arquivo)):
            link = self.url + url_arquivo[number_link].replace("blob","raw")
            HTML = self.accessWeb(link)
            code_boladao = HTML.text
            print("| [" + frescurinha.OKBLUE + "USER" + frescurinha.ENDC + "]: %s" % usuario[number_link])
            self.saveOutput("| [USER]: %s\n" % usuario[number_link])
            print("| [" + frescurinha.OKBLUE + "LINK" + frescurinha.ENDC + "]: %s" % link)
            self.saveOutput("| [LINK]: %s\n" % link)
            try:
                print("| [" + frescurinha.OKBLUE + "LAST INDEXED" + frescurinha.ENDC + "]: %s" % last_indexed[number_link])
                self.saveOutput("| [LAST INDEXED]: %s\n" % last_indexed[number_link])
            except:
                pass
            self.parseCode(code_boladao)
            if "s" in self.ignora_modulo:
                print(frescurinha.HELP + "+----------------------------------------------------+"+ frescurinha.ENDC)
                self.saveOutput("+----------------------------------------------------+\n")


            #DEBUG DE MLK ZIKA
            #tree_file = html.fromstring(HTML.content)
            #print(tree_file.xpath('//div[contains(@class, "btn-group")]/a[contains(@id, "raw-url")]/@href'))
            #print(frescurinha.OKBLUE + "%s" % link + frescurinha.ENDC)
            #print("%s\n" % HTML.text)

        if not prox_page:
            exit()
        prox_page = prox_page[0]
        prox_page = self.url + prox_page
        self.nextPage(prox_page)

    def accessWeb(self,url_acesso):
        acc = requests.get(url_acesso, headers=self.user_agent)
        if " find any code matching" in acc.text:
            print(frescurinha.FAIL + "[-] We couldn't find any code matching %s\n" % self.args.query + frescurinha.ENDC)
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
        print(frescurinha.HELP + "+[PAGE: 1/%s]-----------------------------------------+" % self.number_page + frescurinha.ENDC)
        self.saveOutput("+[PAGE: 1/%s]-----------------------------------------+\n" % self.number_page)
        self.parseSearch(HTML.content)

try:
    GitMiner().start()
except KeyboardInterrupt:
    print(frescurinha.WARNING + "\n\nBye Bye ;)" + frescurinha.ENDC)
    exit()

##################################################################################
# Easter-Egg? Talvez! Quero deixar um abraco pra toda galera que sempre me apoia
#
# Choko
# SlackDummies
# InurlBR / x27Null
# SlayerOwner
# Rogy153
# Gambler
# Logan
# Coffnix
# Jh00nbr
# Bruno Viadom
# M4dwolf
# g3ol4d0
# canhoto
# AlanSanches
# BlackPirate(LuquinhaMonstroDoPassinhoDoRomano)
# Robertux
# BrenoZika
# Borelli
# Henrique Panda
# Fernando Leitao
# DMR
# Clebeer
# A.Ramos
#
# Toda galera do time RTFM, é muito nego pra dar gr33tz
# sem dúvidas vocês são fodas!
#
# Seus puto, voces sao ph0d4s
##################################################################################
