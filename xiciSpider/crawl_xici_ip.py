import requests
# 使用github库进行随机生成User-Agent
# from fake_useragent import UserAgent
from scrapy.selector import Selector
import pymysql

conn = connection = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='123456',
                                    db='spider',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}


def get_all_page():
    response = requests.get('http://www.xicidaili.com/nn/', headers=headers).text
    selector = Selector(text=response)
    div = selector.css('.pagination')
    all_page = div.css('a::text').extract()
    # 取倒数第二个，也就是最后一页的页数
    last_page = all_page[-2:-1][0]
    return int(last_page)


def crawl_ips():
    # 爬取西刺的免费ip代理
    # ua = UserAgent()
    # headers = {'User-Agent':ua.random}

    # 获取到所有的页数
    last_page = get_all_page()

    for i in range(last_page):
        response = requests.get('http://www.xicidaili.com/nn/', headers=headers).text
        selector = Selector(text=response)
        all_trs = selector.css('#ip_list tr')
        ip_list = []
        # 从第一个开始，去除表头
        for tr in all_trs[1:]:
            speed_str = tr.css('.bar::attr(title)').extract()[0]
            if speed_str:
                speed = float(speed_str.split('秒')[0])
            all_text = tr.css('td::text').extract()

            ip = all_text[0]
            port = all_text[1]
            proxy_type = all_text[5].lower()
            if proxy_type.strip() == '':
                proxy_type = all_text[4].lower()
            print(ip, port, proxy_type, speed)

            ip_list.append((ip, port, proxy_type, speed))
        for ip_info in ip_list:
            cursor.execute(
                '''insert into xici_proxy_ip(ip, port, speed, proxy_type) VALUES ('{0}', '{1}', {2}, '{3}')
                    ON DUPLICATE KEY UPDATE ip=VALUES(ip), port=VALUES(port), speed=VALUES(speed), proxy_type=VALUES(proxy_type) '''
                    .format(ip_info[0], ip_info[1], ip_info[3], ip_info[2])
            )
            conn.commit()


def delete_ip(ip):
    sql = "delete from xici_proxy_ip where ip = '{0}'".format(ip)
    cursor.execute(sql)
    conn.commit()


def judge_ip(ip, port, proxy_type):
    # 判断ip是否可用
    http_url = 'https://www.baidu.com'
    proxy_url = '{0}://{1}:{2}'.format(proxy_type, ip, port)
    try:
        proxy_dict = {
            proxy_type: proxy_url
        }
        response = requests.get(http_url, proxies=proxy_dict, timeout=5)
    except Exception as e:
        print('invalid ip and port')
        delete_ip(ip)
        return False
    else:
        code = response.status_code
        if code >= 200 and code < 300:
            print('effective ip')
            return True
        else:
            print('invalid ip and port')
            delete_ip(ip)
            return False


def get_random_ip():
    # 随机取出ip
    sql = """
        SELECT ip,port,proxy_type FROM xici_proxy_ip
        ORDER BY RAND()
        LIMIT 1
    """
    result = cursor.execute(sql)
    for ip_info in cursor.fetchall():
        ip = ip_info['ip']
        port = ip_info['port']
        proxy_type = ip_info['proxy_type']

    if judge_ip(ip, port, proxy_type):
        return '{0}://{1}:{2}'.format(proxy_type, ip, port)
    else:
        return get_random_ip()


if __name__ == '__main__':
    #pass
    delete_ip('101.224.30.86')
       # crawl_ips()
     #get_random_ip()
