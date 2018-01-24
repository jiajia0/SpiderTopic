# @Time    : 2018/1/15 20:41
# @Author  : Leafage
# @File    : csdnCount.py
# @Software: PyCharm
# @Describe: csdn统计每日博客访问量，定时访问。
import requests
from bs4 import *
import re
import json


def getCurrentCSDN():
    """
    抓取当前的访问量，积分，等级，排名等信息
    :return:
    """
    username = 'test'
    # 主页URL
    URL = 'http://blog.csdn.net/' + username
    # 得到返回的页面数据
    response = requests.get(URL).text
    # 转换为bs4
    soup = BeautifulSoup(response, 'lxml')
    # 得到用户信息相关的内容
    user_result = get_user_info(soup)
    # 得到专栏相关的信息内容
    panel_result = get_panel_info(soup)
    # 得到文章分类的信息内容
    category_result = get_category(soup)

    count_result = {}
    count_result['个人信息'] = user_result
    count_result['专栏信息'] = panel_result
    count_result['文章信息'] = category_result
    save_to_file(count_result)


def save_to_file(result):
    """
    将当前统计的信息与之前的比较并保存
    :param result:
    :return:
    """
    json_info = json.dumps(result, ensure_ascii=False)
    print(json_info)



def get_user_info(page_soup):
    """
    统计出当前访问量、积分、等级、排名等信息
    :param page_soup:
    :return:
    """
    # 找到个人数据信息的部分
    user_info = page_soup.find('ul', id='blog_rank').find_all('li')

    user_result = {}

    # 找到访问的数量
    visit_num = user_info[0].text
    user_result['访问'] = get_re_num(visit_num)
    # 找到积分
    points = user_info[1].text
    user_result['积分'] = get_re_num(points)
    # 找到等级
    level = user_info[2]('img')[0]['src']
    user_result['等级'] = get_re_num(level)
    # 找到排名
    rank = user_info[3].text
    user_result['排名'] = get_re_num(rank)
    return user_result


def get_panel_info(page_soup):
    """
    得到专栏的文章量和访问量
    :param page_soup:
    :return:
    """
    # 得到专栏的所有信息
    panel_info = page_soup.find('ul', id='sp_column').find_all('td')[1::2]
    # 保存所有的专栏信息
    panel_result = {}
    # 遍历所有的专栏内容
    for panel in panel_info:
        panel_example = {}
        # 得到专栏名称
        panel_name = panel('a')[0].text
        # 得到专栏的文章数量
        panel_article_num = panel('p')[0].text
        # 得到专栏的访问量
        panel_visit_num = panel('span')[0].text
        # 将信息进行保存
        panel_example['文章'] = get_re_num(panel_article_num)
        panel_example['阅读'] = get_re_num(panel_visit_num)
        panel_example['平均'] = int(get_re_num(panel_visit_num)) / int(get_re_num(panel_article_num))
        panel_result[panel_name] = panel_example
    return panel_result


def get_category(page_soup):
    """
    得到文档分类的数据量
    :param page_soup:
    :return:
    """
    # 得到所有分类文章的列表
    category_info = page_soup.find_all('div', id='panel_Category')[1].find_all('ul')[1].find_all('li')
    category_result = {}
    # 处理所有的分类文章
    for category in category_info:
        category_example = {}
        # 分类名称
        category_name = category('a')[0].text
        # 该分类的文章数
        category_article_num = category('span')[0].text
        category_article_num = get_re_num(category_article_num)
        # 分类的链接
        category_link = category('a')[0]['href']
        # 得到该分类的所有访问量
        category_sum = get_category_sum(category_link)
        category_example['文章'] = category_article_num
        category_example['访问'] = category_sum
        category_example['平均'] = int(category_sum) / int(category_article_num)
        category_result[category_name] = category_example
    return category_result


def get_category_sum(link):
    """
    统计该链接下的所有文章访问总和
    :param link:
    :return:
    """
    num = 0
    url = 'http://blog.csdn.net' + link
    category_page = requests.get(url).text

    category_page = BeautifulSoup(category_page, 'lxml')

    # 得到当前页所有文章的列表
    article_list = category_page.find('div', id='article_list').find_all('span', class_='link_view')

    for article in article_list:
        num += int(get_re_num(article.text))

    # 得到下一页的链接
    pape_list = category_page.find('div', id='papelist')
    if pape_list is not None:
        pape_list = pape_list('a')[-2]
    else:
        return num

    # 如果倒数第二个不等于下一页的话，说明此时已经是最后一页了
    if pape_list.text != '下一页':
        return num
    else:
        # 否则的话递归调用
        return num + get_category_sum(pape_list['href'])


def get_re_num(string):
    """
    从string中找到num
    :param string:
    :return:
   """
    num = re.match(r'.*?(\d+)', string)
    return num.group(1)


if __name__ == '__main__':
    getCurrentCSDN()