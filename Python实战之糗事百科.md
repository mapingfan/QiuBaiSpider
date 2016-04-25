# Python实战之糗事百科

标签（空格分隔）： Python实战记录

---

本文用来记录和总结爬去糗事百科时遇到的坑以及如何出坑。

在写爬糗百的爬虫之前，我已经爬过几个网站，并且都是英文站点。为何会怕英文网站，因为我发现爬中文站点会遇到各种各样的编码问题，当时我是很烦这些编码问题，故此一心躲避。但是祸躲不掉，英文网站同样遇到了各种字符编码问题，比如欧洲某些国家的字符是带重音的，如果你不了解编码的转换，那么编码问题你还是会头疼。后来我仔细研究了下编码问题，主要途径就是谷歌搜对应的错误类型。后来看了几篇文章，对编码问题也有一定的了解。`Python 2.x`系列的编码的确设计的不怎么好，存在天生性的缺陷，但是都有对应的解决办法。关于编码问题的详细总结我已经记录在另一篇文章里，这里简要的写一下处理编码问题的思路。编码问题根源在于输入和输出的编码格式不一致，只要把格式转换一致就不会出现问题，至少我现在是没遇到过解决不了的编码，不排除以后发现新大陆。

上面写的是编码问题，下面总结下写码过程中遇到的一些问题：
1.第一个问题就是使用正则表达式。我忘记了加上参数`re.S`，导致`.`号不能匹配换行符。
2.第二个坑是用`BeautifulSoup`处理页面时候遇到的。因为页面中存在`<!-->`即注释内容，导致使用某些函数可能会出错，这一点在库文档中也明确提到过，要慎重对待注释内容。如果注释内容不重要，记得提前滤去注释。
3.第三个问题仍然和字符编码有关。那就是当我使用`# coding = utf-8`时（注意等号后面有空格），强迫症发了，在等号后面擅自加了一个空格，但是这条注释不能正确识别。一定不要加空格！

下面是设计思路的问题：
经过几次摸索，以及最近对算法的学习，我对写代码有了一些理解。或许谈不上理解，只是对前辈给的忠告表示认同。以前写代码，拿到手就写，不想清楚问题就写，或者是遇到问题感觉烦。不想清楚就写会倒是写代码思路混乱，分不清模块或者更严重的是无法实现功能。遇到问题感觉烦而不是想方法解决问题的确一个很严重的问题，尤其对学计算机专业的学生来说。几经折腾，我发现画个`UML`图或者草图，理清模块之间关系，理清功能实现的流程的确是至关重要的。以前我也听说正规开发要写文档，画流程图等，当时不屑一顾。但是代码写的越多你就会发现理清流程是多么重要。现在每次写代码我都会想一想，自己要解决什么问题，解决问题可以分为哪些步骤，每个步骤要对应哪些函数。把需要的函数，库，设计的主要变量名都是列在代码起始处的注释里。
然而不要试图认为自己一次性就能想清处所有的流程。我们可以做到把总体的流程框架画出，但是具体实现的时候可能会出现一些小问题。就拿此次写爬虫为例，我原本的设计思路是:抓取页面->提取页面内容->存储页面。从大的方向上的确没错，我还为此设计了对应的函数。fetch_page/get_page/sotre_page.但是实际处理过程中，我还加了些预处理过程，比如去除页面中的空格，注释，过滤某些内容。所以，要灵活把握自己的设计过程。我在知乎上看到一句话很有意思，这里分享下：‘对于某些不好实现的需求，放到最后，说不定最后需求就变了’。当然就写爬虫来说，我也是做了些妥协，比如当我采用面向过程的设计方法时，我一时间没找到好的方法滤去带图片的段子，故此搁置放到了最后。但是后来我想到了方法进行过滤。在实现需求的时候要灵活调度。
总结下上面的这么多废话：灵活设计需求，灵活实现需求。

下面说下面向过程设计和面向对象设计：
说实话，我感觉面向过程设计更符合人的习惯，也许只是我的习惯（针对爬虫来说）。因为我们已经很熟悉爬虫的过程了，爬取，提取，存储。我们很自然为它定义了三个函数。但是面向过程给我一种感觉就是太松散，这一段，那一段。
后来我又用面向对象的方法写了一遍。要用面向对象解决问题，首先要想明白我们面向的就究竟是谁，对象有什么属性，方法。这些问题是一定 要在写代码之前设计好的，否则后期可能会有很大改动。对于爬虫来说，我们可以很容易的想到，我们爬取对象是网页，那么我们很自然的就会知道我们面向的是网页。那么考虑下网页的属性，无非就是`URL`以及一些参数。方法也可以很容易确定下来，无法抓取，保存，提取，预处理。面向对象实现给人感觉就是很紧凑，因为各种方法属性都集中在一个类里。不得不承认面向对象有其威力。
说到这里，说的感悟吧。一起我学`C++`的时候，当时也讲面向对象，但是始终不得要领，但是这个爬虫写完了，我确有点领会。所以有时候当时学不会的知识不如暂时搁置（当时理解不了可能碍于心智，理解能力，场景等问题），说不定哪天写着写着你就知道如果面向对象了。
关于实现的代码底下会附上，还有很大改进空间的吧，但是感觉玩够了，使用我决定开始爬别的网站，根据进度，下一个应该是爬百度贴吧。

最后来个总结，总结下得失。其实对现阶段的我来说，失去的只有时间了，因为自己偷懒，拉长了战线，浪费了不少时间。以前感觉不到时间的珍贵，但是到了大三，才发现时间过的真快。以前感觉自己啥都缺，唯独不缺时间，现在感觉自己时间也很缺。时间不多，我已不想浪费时间在无意义的事情上。最近一个月，我唯一的感悟就是要平静你的心，拓展的你的视野。我是一个很狂躁的人，内心不平静，我注定做不好任何事情。对我来说，内心平静的方法就是少接触那些分散注意力，精力的事情。这是我对自己的告诫，希望我能时刻记住这句话。写了好几个爬虫肯定是有收获的。我对面向对象，面向过程的设计方法有了更深的理解。其次就是学到了很多网络方面的知识。最后很重要的一点就是关于学习层面的，如何写代码。写代码之前设计好思路，这样才更容易实现自己的需求。这个不是仅针对项目来说，平时的写作业，刷题也是如此。关于如何得到解体思路，这个问题也许需要更长远的思考。我目前掌握的就是从数学解题中学到的，根据已知推导结论。对应到写代码中，已知可以认为是我们已经学会的程序设计知识，结论可以类比需求的实现。这是我第一次做小项目，所以写了点东西记录下。文中可能有诸多错误，还望海涵。
  莫利斯安 写于2015年11月7日21:29:27

实现代码：
上面的是`面向过程`设计，很大注释就略去了，因为涉及思路文中都提到了。代码仅供参考，有问题可以和我交流。
```Python
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


```
接下来是`OOP`设计
```Python
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


```
