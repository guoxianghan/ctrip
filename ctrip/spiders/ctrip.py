# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
#import codecs
#import sys
#reload(sys)
#sys.setdaulftencoding('utf-8')
#from ctrip.items import CtripItem


class ctrip(scrapy.Spider):
    name="m.ctrip.com"
    start_urls=[
            #"http://m.ctrip.com/html5/mkt/sitemap/index.html"
        'http://m.ctrip.com/html5/hotel/sitemap-domestic'
        ]
    def parse(self, response):
        print  '================================================================'
        print response.headers['Content-Type']
        print  '================================================================'
        hxs = HtmlXPathSelector(response)
        li=  hxs.select("//a")
        print  '================================================================'
        print  li.__len__()
        print  '================================================================'
        items = []
        for a in li:
            #item = CtripItem()
            #item['title']=a.select('@href').extract()
            #item['url']=a.select('@title').extract()
            #items.append(item)
            #print item['title'],'',item['url']
            #unicode.encode(a.select('@title').extract(), 'utf-8');
            #print unicode(a.select('@title').extract())
            try:
                print a.select('@href').extract(),'  ', a.select('@title').extract()[0]
            except IOError:
                pass
            else:
                pass
            pass
        print items.__len__()
        #print response.body
        pass