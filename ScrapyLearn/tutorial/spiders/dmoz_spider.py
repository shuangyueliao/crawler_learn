# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
#-*- coding: utf-8 -*-
from scrapy import cmdline
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders.crawl import Rule, CrawlSpider
from scrapy.http.request import Request
from scrapy.selector import HtmlXPathSelector

from items import FjsenItem


class FjsenSpider(CrawlSpider):
    name="fjsen"
    allowed_domains=["fjsen.com"]
    start_urls=['http://www.fjsen.com/j/node_94962.htm']
    rules = (
        Rule(LinkExtractor(allow=r"/j/node_94962\.htm$"), callback="parse_test", follow=True),
        Rule(LinkExtractor(allow=r"/j/node_94962_\d+\.htm$"), callback="parse_test", follow=True),
    )
    def parse_test(self,response):
        try:
            hxs=HtmlXPathSelector(response)
            sites=hxs.select('//ul[@class="list_page"]/li')
            items=[]
            for site in sites:
                item=FjsenItem()
                item['title']=site.select('a/text()').extract()
                item['link'] = site.select('a/@href').extract()
                item['addtime']=site.select('span/text()').extract()
                items.append(item)
                yield item
        except Exception as error:
            print error
        
               
if __name__ == '__main__':
    scrapy.cmdline.execute(argv=['scrapy','crawl','fjsen'])
    print 'scrapy finish'
