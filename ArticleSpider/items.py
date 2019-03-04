# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DongItem(scrapy.Item):
    id = scrapy.Field()
    img_url = scrapy.Field()
    img_url_sash = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()
    commit_num = scrapy.Field()
    img_path = scrapy.Field()
