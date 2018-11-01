# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from wuyun_crawl.items import WuyunCrawlItem
import logging

class WuyunSpider(CrawlSpider):
    name = 'wuyun'
    allowed_domains = ['www.cnvd.org.cn']
    start_urls = ['http://www.cnvd.org.cn/flaw/list.htm']

    page_extractor = LinkExtractor(allow="offset=\d+")
    detail_extractor = LinkExtractor(allow="CNVD-\d+-\d+")

    rules = (
        Rule(page_extractor, follow=True),
        Rule(detail_extractor, follow=True, callback="parse_content")
    )

    def parse_content(self, response):
        # logging.error(response.url)
        item = WuyunCrawlItem()
        item["title"] = response.xpath('//div[@class="blkContainerSblk"]//h1//text()').extract()[0].strip()
        item["cnvd_id"] = response.xpath('//table[@class="gg_detail"]//tr[1]//td[2]//text()').extract()[0].strip()
        item["push_time"] = response.xpath('//table[@class="gg_detail"]//tr[2]//td[2]//text()').extract()[0].strip()
        item["detail_url"] = response.url

        yield item
