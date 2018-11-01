# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import logging

class WuyunCrawlPipeline(object):
    def process_item(self, item, spider):
        # print(json.dumps(item.__dict__, ensure_ascii=False))
        pass