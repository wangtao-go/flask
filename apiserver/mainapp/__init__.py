
from flask import Flask
import settings
from flask_session import Session


app=Flask(__name__,static_folder='static',static_url_path='/s') #用/s/css--替代/static/css
#也可以更改setting里面的配置
# STATIC_FOLDER='static'
# STATIC_URL_PATH='/s'


from model import db

db.init_app(app) #初始化应用环境



#从指定的对象中加载flask服务的配置
app.config.from_object(settings.Dev)
session=Session()
session.init_app(app)









