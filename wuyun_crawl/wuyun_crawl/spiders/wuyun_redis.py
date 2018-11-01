#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File  : wuyun_redis.py.py
# @Author: QUANLI
# @Date  : 2018/10/31 16:25
# @Desc  : redis 分布式爬虫示例

from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from wuyun_crawl.items import WuyunCrawlItem
import logging

class WuyunSpider(RedisCrawlSpider):
    name = 'wuyun_redis'
    # allowed_domains = ['www.cnvd.org.cn']
    # start_urls = ['http://www.cnvd.org.cn/flaw/list.htm']
    redis_key = "wuyun:start_urls"

    custom_settings = {
        'ITEM_PIPELINES': {
            # 'wuyun_crawl.pipelines.WuyunCrawlPipeline': 300,
            # 使用scrapy_redis提供的pipline组件，将数据存入redis
            'scrapy_redis.pipelines.RedisPipeline': 300,
        }
    }

    page_extractor = LinkExtractor(allow="offset=\d+")
    detail_extractor = LinkExtractor(allow="CNVD-\d+-\d+")

    rules = (
        Rule(page_extractor, follow=True),
        Rule(detail_extractor, follow=True, callback="parse_content")
    )

    def parse_content(self, response):
        # logging.error(response.url)
        item = WuyunCrawlItem()
        logging.info(response)
        item["title"] = response.xpath('//div[@class="blkContainerSblk"]//h1//text()').extract()[0].strip()
        item["cnvd_id"] = response.xpath('//table[@class="gg_detail"]//tr[1]//td[2]//text()').extract()[0].strip()
        item["push_time"] = response.xpath('//table[@class="gg_detail"]//tr[2]//td[2]//text()').extract()[0].strip()
        item["detail_url"] = response.url

        yield item
