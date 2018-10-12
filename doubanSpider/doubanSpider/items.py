# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    # 电影名称
    movie_name = scrapy.Field()
    # 评分
    movie_star = scrapy.Field()
    # 参评人数
    movie_star_person = scrapy.Field()
    # 简介
    movie_summary = scrapy.Field()
    # 海报
    movie_image = scrapy.Field()
    # 详情界面
    movie_info_url = scrapy.Field()