import requests, json
from bs4 import BeautifulSoup


def paqu1(page):
    url = "https://www.4399dmw.com/search/dh-0-0-0-0-0-{}-0/".format(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
        "Referrer": "www.baidu.com"
    }
    resp = requests.get(url, headers=headers)
    # 保存页面源代码
    html_doc = resp.content.decode('utf-8')
    # 使用bs去处理网页源代码
    soup = BeautifulSoup(html_doc)
    list = soup.find('div', class_='lst').find_all('a', class_='u-card')
    for itme in list:
        name = itme.find('p', class_='u-tt').string
        imageadd = itme.find('img').get('data-src')
        inurl = itme.find('a')
        data = name + '------' + 'https:' + imageadd
        print(data)
def main():
    for i in range(10):
        tishi = f'开始爬取第{i}页'
        print(tishi)
        paqu1(i)


    pass

if __name__ == '__main__':
    main()
