import scrapy
from test1.items import Test1Item


class Spider1Spider(scrapy.Spider):
    # 爬虫根据这个名字运行
    name = "spider1"
    # 允许的域名
    allowed_domains = ["4399dmw.com"]
    # 从什么域名开始
    start_urls = ["https://www.4399dmw.com/search/dh-5-0-0-0-0-1-0/"]

    def parse(self, response):
        datas_pic = response.xpath("//a[@class='u-card']/img")
        for item in datas_pic:
            # 使用items来存储
            pic = item.xpath("@data-src").extract()
            title = item.xpath("@alt").extract()
            topipline1 = Test1Item(pic=pic, title=title)
            yield topipline1

