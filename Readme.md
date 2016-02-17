# findFreeEbooks
findFreeEbooks 是为 Alfred 开发的一款 workflow，目的是实现免费电子书的快速查询，在一个动作中完成对多个站点的搜索。目前收录的站点为：[Readfree][1]和[读远][2]

# Development
Alfred 2的 workflow 提供了多种实现方式，比如shell、php、perl、python、ruby和applescript。
findFreeEbooks 是基于 Python2.7 开发的。

通过 urllib2 和 BeautifulSoup 解析，检索完成后通过 python 输出 Alfred 2能识别的 xml。

# Requirements
* Python2.7 （OS X 默认的 Python 版本）
* Alfred 2（付费版）
* 第三方库：BeautifulSoup

# Installation
下载 findFreeEbooks.alfredworkflow，双击导入 Alfred 2 即可。

# How to use
* 通过 option+space 呼出 Alfred，输入 book＋关键字，进行搜索。
* 输入 book＋Help 打开本帮助文档
* 用 上下方向键 或 command+数字，回车可以直接在默认浏览器打开。

# More about me
* 我的个人博客：chanjh.com
* 如果你有更多免费图书资源站，欢迎分享，我再把它加到 workflow 中。

[1]:	http://readfree.me
[2]:	http://readcolor.com/ "http://readcolor.com"