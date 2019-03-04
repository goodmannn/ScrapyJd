import pymysql


class Base():
    conn = None
    host = 'localhost'
    user = 'root'
    pwd = 'lujian123'
    port = '3306'
    db = 'test'

    def __init__(self):
        if not self.conn:
            conn = pymysql.connect(host=self.host, user=self.user, passwd=self.pwd, db=self.db, port=3306,
                                   charset='utf8')
            self.conn = conn

    def test(self):
        type(self.conn)
        pass
