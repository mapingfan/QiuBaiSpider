# coding=utf-8
import re
import urllib2
from bs4 import BeautifulSoup
__author__ = 'Max'

# we use OOP to implement the spider .
# All attributes: url page_number
# All methods: get_content pretreatment save_file fetch_page
# All library: urllib2 re BeautifulSoup


class QiuShiBaiKe:
    def __init__(self, base_url):
        self.base_url = base_url

    @staticmethod
    def save_file(filename, content):
        temp_file = open(filename, 'w')
        temp_file.write(content)
        temp_file.close()

    def fetch_page(self, page_num):
        request = urllib2.Request(self.base_url+str(page_num))
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        request.add_header('User-Agent', user_agent)
        try:
            fetched_html = urllib2.urlopen(request).read()
            self.save_file('fetched.html', fetched_html)
        except urllib2.URLError as e:
            if hasattr(e, 'reason'):
                print 'The reason is ', e.reason
            if hasattr(e, 'code'):
                print 'The error code is ', e.code
            else:
                print 'Something strange happened '

    @staticmethod
    def pretreatment(html):
        temp_file = open(html).read()
        pattern_comment = re.compile(r'<!.*?-->', re.S)
        comment_file = pattern_comment.sub('', temp_file)
        soup = BeautifulSoup(comment_file, 'lxml')
        result = soup.find_all('div', class_='thumb')
        for index in range(0, len(result)):
            result[index].parent.decompose()
        return soup

    @staticmethod
    def get_content(html):
        soup = QiuShiBaiKe.pretreatment(html)
        title = soup.find_all('h2')
        body_content = soup.find_all('div', class_="content")
        stats_vote = soup.find_all('span', class_="stats-vote")
        stats_comment = soup.find_all('a', class_="qiushi_comments")
        for index in range(0, len(title)):
            print (u'第%s楼:' % (index + 1)).encode('gbk', 'ignore')
            print title[index].get_text().encode('gbk', 'ignore')+':'
            print body_content[index].get_text().strip().encode('gbk', 'ignore')
            print (stats_vote[index].i.string+u' 人点赞 ' + stats_comment[index].i.string+u' 人评论').encode('gbk', 'ignore')
            print u'-----------------------------我是华丽的分割线-----------------------------'.encode('gbk', 'ignore')

    def start(self):
        print u"""
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        ++                      欢迎阅读糗事百科                                 ++
        ++                   正在为您加载第一页的段子......                       ++
        ++                     加载完毕，敬请欣赏......                          ++
        ++            输入quit退出，按任意键加载下一页段子。                        ++
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """.encode('gbk', 'ignore')
        page_num = 1
        while True:
            self.fetch_page(page_num)
            self.get_content('fetched.html')
            test_quit = raw_input(u'输入quit退出，按回车加载下一页段子.'.encode('gbk', 'ignore'))
            if test_quit == "quit":
                break
            else:
                page_num += 1
        print u'正在退出糗事百科......'.encode('gbk', 'ignore')


test_base_url = 'http://www.qiushibaike.com/hot/page/'
test_spider = QiuShiBaiKe(test_base_url)
test_spider.start()
