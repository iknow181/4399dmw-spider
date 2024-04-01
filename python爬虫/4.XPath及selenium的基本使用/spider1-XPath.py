import requests, json
from lxml import etree


# 爬取内容
def pachong(url):
    html = get_etree(url)
    dongmantitle = html.xpath("//div[@class='u-ct']/p[@class='u-tt']/text()")
    domgmanimg = html.xpath("//div[@class='lst']/a/img/@data-src")
    for i in range(len(dongmantitle)):
        print(f'{dongmantitle[i]}----http:{domgmanimg[i]}')


# 爬取下一页链接
def find_next_page(url):
    html = get_etree(url)
    # 获取下一页的链接
    next_page = html.xpath("//a[contains(text(),'下一页')]/@href")
    # 创建完整的地址
    really_next_page = 'http://www.4399dmw.com' + next_page[0]
    return really_next_page


# 获得element对象
def get_etree(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
        "Referrer": "www.baidu.com"
    }
    resp = requests.get(url, headers=headers)
    html_doc = resp.content.decode('utf-8')
    # 使用etree去转化html_doc，转化为一个html对象，此时element对象可以使用xpath语法
    html = etree.HTML(html_doc)
    return html


def main():
    url = "https://www.4399dmw.com/search/dh-0-0-0-0-0-1-0/"
    page_num = 1
    while True:
        try:
            print(f'开始爬行第{page_num}页:{url}')
            pachong(url)
            url = find_next_page(url)
            page_num += 1
            print('-' * 20)
        except:
            break
    print('爬取结束')
    pass


if __name__ == '__main__':
    main()
