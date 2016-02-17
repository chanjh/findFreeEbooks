# -*- coding: utf-8 -*-


import urllib2
from bs4 import BeautifulSoup

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

__author__ = 'ChanJH.com'


def main():
    
    url1 = 'http://readfree.me/search/?q='
    urldoc1 = urllib2.urlopen( url1 + theQuery ).read()
    url2 = 'http://readcolor.com/books/search?utf8=%E2%9C%93&s='
    urldoc2 = urllib2.urlopen( url2 + theQuery ).read()

    # 通过这两个关键字，检索搜索到的书籍数量
    count1 = urldoc1.count("class=\"pjax\"")/2
    count2 = urldoc2.count("class=\"book thumbnail\"")

    if count1+count2 == 0:	#搜索不到任何书籍
        xmldoc = "<?xml version=\"1.0\"?>\n<items>"
        xmldoc += "<item uid=\"Books\" arg=\"\">\n<title>没有找到任何有关\""+theQuery+"\"的书籍</title>\n<subtitle>请检查你的关键字，或更换搜索内容。更多帮助可以输入 Help</subtitle>\n<icon>icon.png</icon></item>"
        xmldoc += "</items>\n"
        print xmldoc

    else:
        # 初始化返回值
        xmldoc = "<?xml version=\"1.0\"?>\n<items>"

        xmldoc,links1 = readFree(urldoc1,xmldoc)
        xmldoc,links2 = duYuan(urldoc2,xmldoc)

        # 返回值尾巴
        xmldoc += "<item uid=\"Books\" arg=\"\">\n<title>有关\""+theQuery+"\"的结果"+str(len(links1)+len(links2)-1)+"个条</title>\n<subtitle></subtitle>\n<icon>icon.png</icon></item>"
        xmldoc += "</items>"
            
        print xmldoc

def duYuan(urldoc2,xmldoc):
    soup = BeautifulSoup(urldoc2)

    # 获取作者数组
    authors = []
    for author in soup.find_all("li"):
        if author.get_text(strip=True).find("作者") !=-1 :
            authors.append(author.get_text(strip=True))
        else:
            continue

    # 获取链接和书名
    links = []
    for link in soup.find_all('a','book thumbnail'):
        links.append(link.get('href'))
        title = link.get('title')
        xmldoc += "<item uid=\"Books\" arg=\""+link.get('href')+"\">\n<title>"+title+"</title>\n<subtitle>"+authors[len(links)]+"｜来源：读远</subtitle>\n<icon>icon.png</icon></item>"

    return xmldoc,links

def readFree(urldoc1,xmldoc):
    soup = BeautifulSoup(urldoc1)

    # 获取作者数组
    authors = []
    for author in soup.find_all('small'):
        if author.get_text(strip=True) == "0":
            continue
        else:
            authors.append(author.get_text(strip=True))
    
    # 获取链接和书名
    links = ['None']
    for link in soup.find_all('a','pjax'):
        if link.get('href') == links[-1] :
            continue
        else :
            links.append(link.get('href'))
            title = link.find('img').get('alt')
            xmldoc += "<item uid=\"Books\" arg=\"http://readfree.me"+link.get('href')+"\">\n<title>"+title+"</title>\n<subtitle>作者："+authors[len(links)-2]+"｜来源：readfree.me</subtitle>\n<icon>icon.png</icon></item>"
    return xmldoc,links

def youNeedHelp():

    xmldoc = "<?xml version=\"1.0\"?>\n<items>"
    xmldoc += "<item uid=\"Books\" arg=\"https://github.com/chanjh/findFreeEbooks/blob/master/Readme.md\">\n<title>打开帮助</title>\n<subtitle>回车打开网页，查看详情帮助</subtitle>\n<icon>icon.png</icon></item>"
    xmldoc += "</items>\n"
    print xmldoc

theQuery = "{query}"
if theQuery.lower() == "help" :
    youNeedHelp()
else:
    main()