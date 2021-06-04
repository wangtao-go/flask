from flask import Flask

#创建flask对象-Httpd WEB服务对象
app = Flask(__name__) #__name__可以是任意小写字母，表示flask应用对象名称
#也

from flask import request,render_template

#restful设计风格中关于资源的动作'GET','POST'
@app.route('/',methods=['GET','POST'])#声明web服务的请求资源（指定资源访问的路由）
def hello_world():

    #wsgi->QUERY_STRING:username=disen&password=123,
    #flask封装好的request方法的arg可以直接获取wsgi中的参数
    name=request.args.get('username')
    password=request.args.get('password')

    return 'Hello World!'

# #Flask的MVC设计思想
# 1.客户端发起请求之后，通过路由器找到试图处理函数
# 2.路由和试图处理函数（controller）
# 3.在视图的处理函数中根据业务需求，加载数据（model）并渲染到模版中（view）
# 4.将渲染之后的模版数据返回给客户端
from flask import abort
@app.route('/bank',methods=['GET','POST'])
def addBank():

    data={
        'title':'card',
        'error_message':''
    }
    #渲染模版
    if request.method=='POST':

        #处理POST请求，获取表单参数
        name=request.form.get('name',None)
        print(name)
        card_num=request.form.get('card_num',None)
        print(card_num)
        if all((name,card_num)):
            return 'Hello World!'
        data['error_message']='银行名称不能为空'

    return render_template('bank_edit.html',**data)




if __name__ == '__main__':
    #启动服务，相当于wsgi的make_server

    app.run('localhost',5000,True,
            threaded=True)





