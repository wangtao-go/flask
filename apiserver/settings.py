from redis import Redis


class Dev():

    #默认运行环境production
    ENV='development'
    SECRET_KEY='ananj*&'

    #配置session
    SESSION_TYPE='redis'

    SESSION_REDIS=Redis(host='localhost',port=6379,db=2)

    #配置sqlalchemy数据库连接及特征
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Wtao648588129!@localhost:3306/bank?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATION=True #设置可扩展
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True #回收资源时自动提交事务
    SQLALCHEMY_ECHO=True #显示调试SQL


class Product():
    # 默认运行环境production
    ENV = 'production'
    SECRET_KEY = 'ananj*&'







