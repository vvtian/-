import scrapy
from scrapy.http.response.html import HtmlResponse
from ..items import DoubanbookItem    #导入items

class DoubanbookSpider(scrapy.Spider):
    name = 'doubanbookspider'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']

    def parse(self, response:HtmlResponse):     #如何解析HTML   返回一个可迭代对象
        #items=[]
        subjects = response.xpath('//li[@class="subject-item"]')
        for subject in subjects:
            item=DoubanbookItem()      #当作是个字典
            title = subject.xpath('.//h2/a/text()').extract()
            item['title']=title[0].strip()

            rate = subject.css('span.rating_nums::text').extract()
            item['rate']=rate[0].strip()

            #items.append(item)
            yield item

        #with open('D:\PythonProjects\myspider\doubanbook\doubanbook.txt','w',encoding='utf-8') as f:
            #for item in items:
                #f.write('{} {}\n'.format(item['title'],item['rate']))

        #return items