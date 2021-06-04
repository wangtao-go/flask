import math

from flask import render_template
from flask import Flask
from mainapp import app
#导入的app是mainapp的__init__.py定义的Flask(__name__)对象

from flask_script import Manager
from mainapp.views import bank,user,card,book

@app.template_filter('date_change')
def date_change_filter(value,*args):
    print(value,type(value),args)
    return value.strftime(args[0])


@app.template_filter('moneyfmt')
def moneyfmt_filter(value,method='common',precision=0):
#'common'普通的金额的格式化
    value=round(value,precision)
    if method=='common':
        #以千位符分
        if isinstance(value,int):
            pre_v=str(value)
            end_v=''
        else:
            pre_v,end_v=str(value).split('.')
        pre_v=pre_v[::-1]
        vs=[pre_v[i*3:i*3+3] for i in range(math.ceil(len(pre_v)/3))]

        return ','.join(vs)[::-1]+'.'+end_v
    return value



@app.errorhandler(404)
def notfounded(error):
    print(error)
    return render_template('404.html')


from flask_cors import CORS

if __name__ == '__main__':
    CORS().init_app(app)
    # 蓝图建立好后，需要注册到flask服务中
    app.register_blueprint(bank.blue)
    app.register_blueprint(user.blue)
    app.register_blueprint(card.blue)
    app.register_blueprint(book.blue,url_prefix='/book')
    manager=Manager(app)
    manager.run()













