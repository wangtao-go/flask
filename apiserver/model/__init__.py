import pymysql
from pymysql.cursors import DictCursor
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()




CONFIG = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Wtao648588129!',
    'db': 'bank',
    'port': 3306,
    'charset': 'utf8',
    'cursorclass': DictCursor,
}


class DB():
    def __init__(self):
        self.conn = pymysql.Connect(**CONFIG)

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None


class BaseModel():
    def __init__(self):
        self.db = DB()

    def find_all(self, table, where=None, *whereArgs):
        sql = "select * from %s" % table
        if where:
            sql += where
        with self.db as c:
            c.execute(sql, whereArgs)
            result = list(c.fetchall())
        return result

    def save(self,table,**data):
        sql="insert into %s(%s) values (%s)"
        colnames=','.join([key for key in data])
        colpalceholdes=','.join(['%%(%s)s' % key for key in data])
        with self.db as c:
            c.execute(sql %(table,colnames,colpalceholdes),data)
            if c.rowcount>0:
                return True
        return False


    def update(self,table,b_id,**data):
        sql='update %s set %s where b_id=%s'
        update_cols=','.join(['%s=%%(%s)s' % (key,key) for key in data])
        with self.db as c:
            c.execute(sql %(table,update_cols,b_id),data)
            if c.rowcount>0:
                return True
        return False

