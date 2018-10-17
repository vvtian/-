from scrapy.http.response.html import HtmlResponse

response=HtmlResponse('file://D:\PythonProjects\myspider\doubanbook\doubanbook.html',encoding='utf8')

with open('D:\PythonProjects\myspider\doubanbook\doubanbook.html',encoding='utf8') as f:
    response._set_body(f.read().encode())
    #print(response.text)
    #解析
    subjects=response.xpath('//li[@class="subject-item"]')
    #xpath
    for subject in subjects:
        #print(subject)
        title= subject.xpath('.//h2/a/text()').extract()   # selectorlist类型
        #print(type(title))
        print(title[0].strip())

        rate=subject.xpath('.//span[@class="rating_nums"]/text()')
        print(rate[0].extract().strip())    #lxml

    #css
    for subject in subjects:
        title = subject.css('h2 a::text')
        print(title[0].extract().strip())

        rate = subject.css('span.rating_nums::text').re(r'^9\..*')  #9分以上
        if rate:
            print(rate[0].strip())

