import pymysql


class Base():
    databases = None
    host = '192.168.31.250'
    user = 'root'
    pwd = 'anbs,23t'
    port = '3306'
    db = 'test'

    def __init__(self):
        conn = pymysql.connect(host=self.host, user=self.user, passwd=self.pwd, db=self.db, port=3306,
                               charset='utf8')
        self.databases = conn.cursor()
        self.conn = conn
