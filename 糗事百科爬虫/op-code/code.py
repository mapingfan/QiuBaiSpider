# coding=utf-8
import urllib2
from bs4 import BeautifulSoup
import re
__author__ = 'Max'
# First ,we import all the library we need .
# we use BeautifulSoup to deal with the page .
# We fetch the page .
# Function signature : fetch_page(url)


def save_file(filename, content):
    temp_file = open(filename, 'w')
    temp_file.write(content)
    temp_file.close()


def fetch_page(url, page_num):
    req = urllib2.Request(url+str(page_num))
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    req.add_header("User-Agent", user_agent)
    try:
        response = urllib2.urlopen(req)
        html = response.read()
        save_file('story.htm', html)
    except urllib2.URLError as e:
        if hasattr(e, 'reason'):
            print 'The reason is :', e.reason
        elif hasattr(e, 'code'):
            print e.code
        else:
            print 'Something strange happened .'

# second ,pretreatment .
# Before we get what we need, we delete something like pics and comments in the html .


def pretreatment(page):
    html = open(page).read()
    pattern_comment = re.compile(r'<!--.*?-->', re.S)
    pattern_pic = re.compile(r'<div class="thumb">.*?</div>', re.S)
    pattern_sub_result = pattern_comment.sub('', html)
    pattern_pic_result = pattern_pic.sub('', pattern_sub_result)
    save_file('pretreatment.htm', pattern_pic_result)


def get_content(page):
    qiu_soup = BeautifulSoup(open(page), 'lxml')
    content = qiu_soup.find_all('div', class_="content")
    name = qiu_soup.find_all('h2')
    stats_vote = qiu_soup.find_all('span', class_="stats-vote")
    comment = qiu_soup.find_all('a', class_="qiushi_comments")
    for index in range(0, len(name)):
        print u'作者:'.encode('gbk', 'ignore')+name[index].string.encode('gbk')
        print content[index].get_text().strip() .encode('gbk')
        print stats_vote[index].i.string.encode('gbk', 'ignore') + u'人支持 '.encode('gbk', 'ignore')
        print comment[index].i.string.encode("GBk", 'ignore'
                                                    ''
                                                    '') + u'人评论'.encode('gbk')
        print '-----------------------------我是华丽的分割线------------------------------'.decode('utf-8').encode('gbk')


def start():
    print """
          ----------------------------------------------------------------------------------
          +                      Welcome to QiuShiBaiKe                                     +
          +                                                                                 +
          + Read the story.if you want something new, please enter any key or quit to exit .+
          ----------------------------------------------------------------------------------
          """
    page_num = 1
    url_para = 'http://www.qiushibaike.com/hot/page/'
    while True:
        fetch_page(url_para, page_num)
        pretreatment('story.htm')
        get_content('pretreatment.htm')
        input_word = raw_input("""
        Page is loading , please have a coffee ....
        The first page has loaded fully ...
        Enter Space to Continue or Input quit to Exit ...

        """)
        if input_word == "quit":
            break
        else:
            page_num += 1

start()
