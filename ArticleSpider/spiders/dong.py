import scrapy
import re
import urllib.parse

from scrapy_splash import SplashRequest

from ..items import DongItem


class DongSpider(scrapy.Spider):
    name = 'dong'
    allowed_domains = ['list.jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=9987,653,655']

    def start_requests(self):
        splash_args = {"lua_source": """
                    --splash.response_body_enabled = true
                    splash.private_mode_enabled = false
                    splash:set_user_agent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
                    assert(splash:go("https://list.jd.com/list.html?cat=9987,653,655"))
                    splash:wait(3)
                    return {html = splash:html()}
                    """}
        yield SplashRequest("https://list.jd.com/list.html?cat=9987,653,655", endpoint='run', args=splash_args,
                            callback=self.parse)

    def parse(self, response):
        dong_item = DongItem()

        product_obj = response.css(".j-sku-item ")

        for product in product_obj:  # type:scrapy.selector.Selector

            """id"""
            product_id = product.css('::attr(data-active-sku)').extract_first()
            if not product_id:
                product_id = product.css('::attr(data-sku)').extract_first()
            """图片地址"""
            img_url = product.css('.p-img a img::attr(src)').extract_first()  # type :str
            if not img_url:
                img_url = product.css('img::attr(data-lazy-img)').extract_first()
            img_url = 'http:' + img_url

            """价格"""
            price = product.css(".p-price strong i::text").extract_first()
            """商品名"""
            product_name = product.css(".p-name a em::text").extract_first().strip()
            """评价数"""
            commit_num = product.css(".p-commit strong a::text").extract_first()
            mth_res = re.match('(^\d+).*', commit_num)
            if mth_res:
                commit_num = mth_res.group(1)
            else:
                commit_num = 0

            dong_item['id'] = product_id
            dong_item['img_url'] = [img_url]
            dong_item['price'] = price
            dong_item['name'] = product_name
            dong_item['commit_num'] = commit_num
            x = dong_item.get('img_url')
            yield dong_item

        next_uri = response.css('.pn-next::attr(href)').extract_first()
        next_url = urllib.parse.urljoin(response.url, next_uri)
        if next_url:
            splash_args = {"lua_source": """
                               --splash.response_body_enabled = true
                               splash.private_mode_enabled = false
                               splash:set_user_agent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
                               assert(splash:go("%s"))
                               splash:wait(3)
                               return {html = splash:html()}
                               """ % next_url}

            yield SplashRequest(next_url, endpoint='run', args=splash_args,
                                callback=self.parse)

    def product_list(self, response):
        pass
