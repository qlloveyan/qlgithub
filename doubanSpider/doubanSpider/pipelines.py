# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import psycopg2

class DoubanspiderPipeline(object):

    def __init__(self):
        # 初始化mysql连接
        db_host = settings["PG_IP"]
        db_port = settings["PG_PORT"]
        db_username = settings["PG_USERNAME"]
        db_password = settings["PG_PASSWORD"]
        db_name = settings["DB_NAME"]

        self.conn = psycopg2.connect(host=db_host, user=db_username, password=db_password, dbname=db_name, port=db_port)

    def process_item(self, item, spider):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO t_movie (name, star, person, summary, info_url, image_url) values (%s, %s, %s, %s, %s, %s)', [item['movie_name'], item['movie_star'], item['movie_star_person'], item['movie_summary'], item['movie_info_url'], item['movie_image']])
        self.conn.commit()
        cursor.close()
        return item

    def close_spider(self, spider):
        self.conn.close()