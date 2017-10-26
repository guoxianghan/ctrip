# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from ctrip.items import CtripItem
from scrapy.http import Request
#import codecs
#import sys
#reload(sys)
#sys.setdaulftencoding('utf-8')
#from ctrip.items import CtripItem

#scrapy crawl m.ctrip.com
class ctrip(scrapy.Spider):
    name = "m.ctrip.com"
    start_urls = [
            #"http://m.ctrip.com/html5/mkt/sitemap/index.html"
        'http://m.ctrip.com/html5/hotel/sitemap-domestic'#all hotels
        ]

    def parse(self, response):
        print('================================================================')
        print(response.headers['Content-Type'])
        print('================================================================')
        hxs = HtmlXPathSelector(response)
        pages = hxs.select("//a[@class='apageing']")
        for p in pages:
            url=p.select('@href')[0].extract()
        yield Request('http://m.ctrip.com'+url, callback=self.getcitylist)
            #purl=p
            #pass
        #li = hxs.select("//a")
        li= hxs.xpath("//a")
        print('================================================================')
        #print(li)
        print(li.__len__())
        print('================================================================')
        items = []
        for a in li:
            item = CtripItem()
            item['title']=a.select('@href').extract()
            item['url']=a.select('@title').extract()
            items.append(item)
            print('item.title='+item['title']+',item.url=',item['url'])
            break
            #unicode.encode(a.select('@title').extract(), 'utf-8');
            #print unicode(a.select('@title').extract())
            try:
                print(a.select('@href').extract(),'  ', a.select('@title').extract()[0])
            except IOError:
                pass
            else:
                pass
            pass
        print(items.__len__())
        #print response.body
        pass
    def getcitylist(self,response):
        print("asdfasdfasdf")
        print(response)
        pass