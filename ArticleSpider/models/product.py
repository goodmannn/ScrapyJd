from ArticleSpider.models.base import Base
import time


class Product(Base):

    def add(self, data):
        sql = "insert into product_1 (id, img_url, price, NAME, commit_num, img_path, img_url_sash, create_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (
            data.get('id'),
            data.get('img_url')[0],
            data.get('price'),
            data.get('name'),
            data.get('commit_num'),
            data.get('img_path'),
            data.get('img_url_sash'),
            int(time.time()))
        self.databases.execute(sql, values)
        self.conn.commit()
        self.databases.close()
        self.conn.close()

        print(1)
