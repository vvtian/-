# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class DoubanbookPipeline(object):
    def __init__(self):
        print('~~~~~~~init~~~~~~~~~~~~~~')

    def process_item(self, item, spider):
        self.file.write('{},\n'.format(json.dumps(dict(item))))    #得到的是Unicode数据
        return item

    def open_spider(self,spider):
        print('______open spider {}_____')
        filename='D:\PythonProjects\myspider\doubanbook\dbbooks2.json'
        self.file=open(filename,'w',encoding='utf-8')
        self.file.write('[\n')

    def close_spider(self,spider):
        print('______close spider {}_____')
        self.file.write(']')
        self.file.close()
