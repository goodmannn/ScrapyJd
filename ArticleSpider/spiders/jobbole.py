import scrapy
import re


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114666/']


    def parse(self, response):
        """

        :param response:
        :return:
        """
        assert isinstance(response,scrapy.http.response.Response)


        """标题"""
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]

        """时间"""
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()')
        create_date = re.match('([\d+]{4}.*[\d+]{2}.*[\d+]{2})', create_date.extract_first()[0].strip())
        if create_date:
            create_date = create_date.group(0)

        """时间"""
        praise_num = response.xpath('//span[contains(@class,"vote-post-up")/h10/text()]').extract()[0]
        collect = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]

        pass
