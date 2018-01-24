import requests
from bs4 import *
from fake_useragent import UserAgent
import random
import time
import crawl_xici_ip
import multiprocessing

# 个人用户名
username = 'test'

# casn刷博客访问量，多了会封号，被警告之后就没有用过了。。。

class getSomething:
    def __init__(self, url, num):
        self.url = url
        self.num = num
        self.agent = UserAgent()
        url_list = self.parse()

        self.saveToFile(url_list, self.startReadNum('http://blog.csdn.net/' + username))

        for i in range(num):
            current_url = 'http://blog.csdn.net' + random.sample(url_list, 1)[0][1]
            try:
                self.addRead(current_url)
            except:
                print('出现异常！')
                pass

        url_list = self.parse()
        self.saveToFile(url_list, self.startReadNum('http://blog.csdn.net/' + username))

    def parse(self):
        url_list = []

        num = 6

        for n in range(1, num + 1):
            url = self.url + str(n)
            page = requests.get(url).text
            soup = BeautifulSoup(page, 'lxml')
            articles = soup.find_all('div', class_='list_item article_item')
            for article in articles:
                title = article.find('div', class_='article_title').text.strip()
                link_title = article.a['href']
                start_readnum = article.find('span', class_='link_view').text
                article_content = [title, link_title, start_readnum]
                url_list.append(article_content)

        return url_list

    def addRead(self, current_url):
        header = {
            'user-agent': self.agent.random
        }
        current_ip = crawl_xici_ip.get_random_ip()
        print(current_ip)
        self.page = requests.get(current_url, headers=header, proxies=current_ip).text
        self.soup = BeautifulSoup(self.page, 'lxml')
        self.readnum = self.soup.find('span', class_='link_view').text[:-3]

        print(self.readnum)

    def saveToFile(self, list, file_name):
        fileName = 'F:\\file\\' + file_name + '.txt'
        with open(fileName, 'w') as a:
            for l in list:
                a.write('Title:' + l[0] + '\ntitle_link:' + l[1] + '\nstart_readnum:' + l[2] + '\n\n')

    def startReadNum(self, url):
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'lxml')
        startNum = soup.find('ul', id='blog_rank').li.text
        return startNum.strip()


if __name__ == '__main__':

    for i in range(1, 2):
        p = multiprocessing.Process(target=getSomething, args=('http://blog.csdn.net/' + username + '/article/list/', 2))
        p.start()
