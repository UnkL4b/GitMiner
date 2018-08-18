import requests
import sys
from core import Parser
from config.banner import colors

def requestPage(url, headers, cookie):
    req = requests.get(url, headers=headers, cookies=cookie)
    #print(req.text)
    if " find any code matching" in req.text:
        print("{RED}\n\n[-] We couldn't find any code matching \n{END}".format(**colors))
        sys.exit()
    return req

def nextPage(next_page, number_page, headers, cookie, config, filename, regex):
        p = Parser.Parser()
        print("{YELLOW}\n+[PAGE %s/%s]-----------------------------------------+".format(**colors) % (next_page.split("&")[1].split("=")[1], number_page))
        content_html = requestPage(next_page, headers, cookie)
        p.getSearch(content_html.content, number_page, headers, cookie, config, filename, regex)
