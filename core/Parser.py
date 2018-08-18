import json
import sys
import re
from lxml import html
sys.path.append('../')
from core.sendRequest import requestPage
from core.sendRequest import nextPage
from config.banner import colors
from config import headers as head


class Parser(object):
    
    def __init__(self):
        # XPATH QUERIES
        self.PAGINATION = '//div[contains(@class, "pagination")]/a/text()'
        self.URLFILE = '//div[contains(@class, "d-flex")]/div[contains(@class, "flex-auto min-width-0 col-10")]/a[2]/@href'
        self.LASTINDEXED = '//div[contains(@class, "d-flex")]/div/div[contains(@class, "flex-column")]/span[2]/relative-time/@datetime'
        self.USER = '//div[contains(@class, "d-flex")]/a[1]/img/@alt'
        self.NEXTPAGE = '//a[contains(@class, "next_page")]/@href'
        
        # URL GITHUB
        self.github_url = 'https://github.com'
        self.github_raw_url = 'https://raw.githubusercontent.com'

    def saveOutput(self, output, filename):
        if filename is not None:
            with open(filename, 'a') as write_file:
                json.dump(output, write_file)
                write_file.write(',')
                write_file.close()


    def parseParameters(self, content_html, _parameters, _splitparam, _splitorder, user, filename):
        param_list = {user:{}}
        for _param in _parameters:
            for line_param in content_html.split("\n"):
                #print(content_html)
                #print(line_param)
                if _parameters[_param] in line_param:
                    _line_param = line_param.replace(_parameters[_param], \
                                 '{BOLD}{RED}%s{END}' % _parameters[_param])
                    print(" {GREEN}+{END} {BOLD}LINE{END}: %s".format(**colors) \
                          % _line_param.format(**colors).strip())
                    for split_order in _splitorder:
                        value_parsed = line_param.split(_splitparam)
                        value_parsed = value_parsed[int(_splitorder[split_order])]
                        print(" {GREEN}+{END} {BOLD}VALUE PARSED{END}: %s\n".format(**colors) \
                          % value_parsed)
                if _parameters[_param] in content_html:
                    for line_param_list in content_html.split("\n"):
                        if _parameters[_param] in line_param_list:
                            for split_order in _splitorder:
                                value_parsed = line_param_list.split(_splitparam)
                                value_parsed = value_parsed[int(_splitorder[split_order])]
                                if _parameters[_param] in param_list[user].keys():
                                    if value_parsed not in param_list[user][_parameters[_param]].values():
                                        count = len(param_list[user][_parameters[_param]]) + 1
                                        param_list[user][_parameters[_param]].update({"%s" % str(count):"%s" % value_parsed})
                                else:
                                    param_list[user].update({"%s" % _parameters[_param]:{"1":"%s" % value_parsed}})
        self.saveOutput(param_list, filename)

    def getContainsFile(self, content_html, _contains):
        print("{GREEN}[+]{END} {BLUE}CONTAIN{END}: ".format(**colors))
        for line_contains in content_html.split("\n"):
            if _contains in line_contains:
                try:
                    line_contains = line_contains.replace(_contains, \
                                    '{BOLD}{RED}%s{END}{ITALIC}' % _contains)
                    print(" {GREEN}+{END} {ITALIC}%s{END}".format(**colors) \
                          % line_contains.format(**colors))
                except:
                    print(" + %s" % line_contains)


    def getRegex(self, content_html, regex):
        match_regex = re.findall( r'{}'.format(regex), content_html, re.M|re.I)
        print("\n{GREEN}[+]{END} {BLUE}REGEX FOUND{END}:".format(**colors))
        for get_regex in match_regex:
            print("{GREEN} + {END} MATCH: %s".format(**colors) % get_regex) 


    def codeParser(self, content_html, config, user, filename, regex):
        _contains = config['contains']
        _parameters = config['parameters']
        _splitparam = config['splitparam']
        _splitorder = config['splitorder']
        if "" != _contains:
            self.getContainsFile(content_html, _contains)
        if _parameters:
            print("\n{GREEN}[+]{END} {BLUE}PARAM FOUND{END}:".format(**colors))
            try:
                self.parseParameters(content_html, _parameters, _splitparam, _splitorder, user, filename)
            except Exception as inst:
                #print(inst)
                pass
        
        if regex is not None:
            self.getRegex(content_html, regex)

        print("\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")


    def getNumPages(self, content):
        tree = html.fromstring(content)
        number_page = tree.xpath(self.PAGINATION)
        if number_page:
            return number_page[len(number_page)-2]
        else:
            return "1"

    def getSearch(self, content, number_page, headers, cookie, config, filename, regex):
        tree = html.fromstring(content)
        url_file = tree.xpath(self.URLFILE)
        last_indexed = tree.xpath(self.LASTINDEXED)
        user = tree.xpath(self.USER)
        next_page = tree.xpath(self.NEXTPAGE)
        headers_raw = head.getHeadersRaw()
        for number_url in range(len(url_file)):
            url_code = self.github_raw_url + url_file[number_url].replace("blob/","")
            content_html = requestPage(url_code, headers_raw, cookie)
            content_html = content_html.text
            print("{GREEN}[+]{END} {BLUE}USER{END}: %s".format(**colors) % user[number_url])
            print("{GREEN}[+]{END} {BLUE}LINK{END}: %s\n".format(**colors) % url_code)
            try:
                print("{GREEN}[+]{END} {BLUE}LAST INDEXED{END}: %s".format(**colors) \
                      % last_indexed[number_url])
            except Exception as inst:
                #print(inst)
                pass
            self.codeParser(content_html, config, user[number_url], filename, regex)

        if not next_page:
            sys.exit() 
        next_page = next_page[0]
        next_page = self.github_url + next_page
        nextPage(next_page, number_page, headers, cookie, config, filename, regex)
