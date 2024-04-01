import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from test1.items import Test1Item


class Spider2Spider(CrawlSpider):
    name = "spider2"
    allowed_domains = ["4399dmw.com"]
    start_urls = ["https://www.4399dmw.com/search/dh-5-0-0-0-0-1-0/"]

    # 决定爬虫的走向,爬到页面是否需要跟进，到某个页面使用什么函数处理
    rules = (
        Rule(LinkExtractor(allow=r".dh-5-0-0-0-0-\d-0\/"), follow=True),
        Rule(LinkExtractor(allow=r".+\/dh\/.+\/"), callback='parse_detail', follow=False)
    )

    def parse_item(self, response):
        #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        #item["name"] = response.xpath('//div[@id="name"]').get()
        #item["description"] = response.xpath('//div[@id="description"]').get()
        datas_pic = response.xpath("//a[@class='u-card']/img")
        for item in datas_pic:
            # 使用items来存储
            pic = item.xpath("@data-src").extract()
            title = item.xpath("@alt").extract()
            topipline1 = Test1Item(pic=pic, title=title)
            yield topipline1


    def parse_detail(self,response):
        title = response.xpath("//div[@class='works__main']/h1/text()").extract()[0]
        jianjie = response.xpath("//div[@class='main']/div/p/text()").extract()[0]
        pic = response.xpath("//div[@class='works__main']//img[@class='works__img']/@data-src").extract()[0]
        topipieline2 = Test1Item(jianjie=jianjie,pic=pic,title=title)
        yield topipieline2
