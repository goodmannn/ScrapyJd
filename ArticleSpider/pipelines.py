# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from ArticleSpider.utils.common import get_md5
import pymysql


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        url = item.get('img_url', '')
        img_url_sash = get_md5(url[0])
        item['img_url_sash'] = img_url_sash

        return item


class DongImgPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        img_path = ''
        for k, v in results:
            img_path = v['path']
        item['img_path'] = img_path
        return item
