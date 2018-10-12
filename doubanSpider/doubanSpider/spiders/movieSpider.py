# -*- coding: utf-8 -*-
import scrapy
from doubanSpider.items import DoubanspiderItem

class MoviespiderSpider(scrapy.Spider):
    name = 'movieSpider'
    allowed_domains = ['movie.douban.com']
    url = "https://movie.douban.com/top250?start="
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        item = DoubanspiderItem()
        movies = response.xpath('//div[@class="item"]')
        for each in movies:
            item["movie_name"] = each.xpath('.//div[@class="hd"]//a//span[1]//text()').extract()[0]
            item["movie_star"] = each.xpath('.//div[@class="star"]//span[2]//text()').extract()[0]
            item["movie_star_person"] = each.xpath('.//div[@class="star"]//span[4]//text()').extract()[0]
            item["movie_summary"] = each.xpath('.//p[@class="quote"]//span[1]//text()').extract()[0]
            item["movie_info_url"] = each.xpath('.//div[@class="pic"]//a//@href').extract()[0]
            item["movie_image"] = each.xpath('.//div[@class="pic"]//a//img//@src').extract()[0]

            yield item

        if self.offset < 250:
            self.offset += 25
        yield scrapy.Request(self.url+str(self.offset), callback=self.parse)