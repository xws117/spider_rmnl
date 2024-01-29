import requests
from bs4 import BeautifulSoup

def response():
    pass

def get_content():
    # 访问能量中国首页，然后返回beautifulsoup处理之后的结果
    url = 'http://www.powerchina.net.cn'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # 'Cache-Control': 'max-age=0',
        'Host': 'www.powerchina.net.cn',
        # 'If-Modified-Since': 'Tue, 23 Jan 2024 06:08:19 GMT',
        # 'If-None-Match': '"3ffb3-b020-60f96c5e49b0d"',
        'Proxy-Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')
    return soup



def get_banner(soup):
    am_slides_div = soup.find('ul',{'class':'am-slides'})
    if am_slides_div:
        # 找到所有在am_slides_div下的li标签
        li_list = am_slides_div.find_all('li')
        
        # 提取每个li下的img的src，并存储在列表中
        img_src_list = [li.find('img')['src'] for li in li_list if li.find('img')]
        
        return img_src_list
    else:
        print("未找到div的class是am-slides")


def get_news(soup):
    news = soup.find('div',{'class':"newt1r"})
    news_img_src_list = []
    news_content_list = []
    news_href_list = []

    if news:
        # 找到所有在news下的li标签
        li_list = news.find_all('li')

        # 提取每个li下的img的src，并存储在列表中
        news_img_src_list = [li.find('img')['src'] for li in li_list if li.find('img')] 

        # 提取文字信息
        news_content_list = [li.text.strip() for li in li_list ] 

        # 提取url信息
        news_href_list = [li.find('a')['href'] for li in li_list if li.find('a')] 

    else:
        print("未找到div的class是newt1r")

    return [news_img_src_list,news_content_list,news_href_list]


def get_idol(soup):

    idol = soup.find('div',{'style':'float:left; width: 33%;margin-left: 2%;margin-top: 10px;'})
    idol_img_src_list = []
    idol_content_list = []
    idol_title_list = []
    idol_href_list = []

    # 获取图片
    if idol:
        # 获取图片
        img_list = idol.find_all('img')
        # print('img_list lenght is :',len(img_list))
        idol_img_src_list = [li['src'] for li in img_list] 

        # 获取title
        a_list= idol.find_all('h3')
        idol_title_list = [li.find('a')['title'] for li in a_list] 
        
        # 获取url
        href_list= idol.find_all('h3')
        idol_href_list = [li.find('a')['href'] for li in href_list] 

        # 获取文字信息
        content_list = idol.find_all('div',{'class':'am-list-item-text'})
        idol_content_list = [li.text.strip() for li in content_list]

    else:
        print('error')

    return [idol_img_src_list, idol_content_list, idol_title_list, idol_href_list]

def get_meaasge(soup):
    # 第六个div才是想要的那个
    message = soup.find_all('div',{'class':'am-g am-g-fixed'})[5]

    message_img_src_list = []
    message_content_list = []
    message_title_list = []
    message_href_list = []

    # print(message)


    if message:
        # 获取图片
        img_list = message.find_all('img')
        # print('img_list lenght is :',len(img_list))
        message_img_src_list = [li['src'] for li in img_list] 


        # 获取title
        a_list= message.find_all('a',{'class':''})
        message_title_list = [li.text.strip() for li in a_list ] 
        message_title_list = [element for element in message_content_list if element != '']

        # 获取文字信息
        content_list = message.find_all('div',{'class':'am-list-item-text'})
        message_content_list = [li.text.strip() for li in content_list]

        # 获取url
        href_list = message.find_all('h3',{'class':'am-list-item-hd'})
        print(href_list)
        message_href_list = [li.find('a')['href'] for li in href_list if li.find('a')]

        
    else:
        print("message error")

    return [message_img_src_list,message_title_list,message_content_list,message_href_list]



soup = get_content()
banner = get_banner(soup)
news = get_news(soup)
message = get_meaasge(soup)
idol = get_idol(soup)
# print(banner)
# print(news)
# print('==='*50)
# print(message)
print(idol)



