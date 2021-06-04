
from flask import Blueprint, make_response, redirect, render_template, session
from flask import request

blue = Blueprint('bankBlue', __name__)


@blue.route('/bank', methods=['GET', 'POST'])
def bank():
    from model.user_login import Bank
    from model.user_login import Card
    data2={"banks":bank.query.all(),
           'card':Card.query.all()}

    # da = banks[0].b_id
    # print('----->')
    # print(da)
    # print(type(da))
    # print('----->')
    # content=locals()
    return render_template('bank_list.html',**data2)



@blue.route('/delbank', methods=['GET'])
def del_bank():
    bank_id = request.args.get('id')
    return "<h3>delete,bank:%s</h3>" % bank_id


# 蓝图建立好后，需要注册到flask服务中


# ----------路由规则---------------
# @app.route('/find/<converter:word>',methods=['GET'])
# def find(word):
#     return ""
# convert是参数的转换器，一般是指定的类型，如:string<不写，直接写后面的>,int,float,path,uuid,any<不写，直接写后面的,表任意类型>
# 其中any比较特殊，可以指定任意类型转化器，如　<any(int,string,uuid):word>
# path转换器主要用于引用别的网址时使用
@blue.route('/bank/publish',methods=['POST'])
def publish_bank():
    data='{"id":102,"age":20}'
    code=200
    #将数据和响应的状态码封装到response
    response=make_response(data,code)

    #根据数据的类型，设置响应头
    response.headers['Content-Type']='apllication/json;charset=utf-8'
    return response

#对于html1，可以使用render_template渲染
# def publish_bank():
#     return '<h3>broadcast bank</h3>',200



@blue.route('/bank/del/<int:bank_id>',methods=['DELETE'])
def deleted(bank_id):
    return '<h2>del success:%s</h2>'%bank_id


@blue.route('/edit/<int:bankId>', methods=['GET'])
def edit(bankId):
    return 'editor now:%s' % bankId


@blue.route('/find/<path:url>', methods=['GET'])
def find(url):
    return """
            <script>
                let steps=5;
                let id=setInterval(
                ()=>{
                if (steps >=1){
                    document.write("<br>left"+(--steps));
                }else{
                    windows.open('%s',target="_self")
                }
                },1000); 
            </script>             
    """ % url


# cookie数据储存技术，它的数据储存在客户端（浏览器），
# 在浏览器中会为每个站点host创建储存
# cookie的空间，以key=value形式储存，但是每个key都有生命周期
# 。一个完整的
# cookie信息包括：名称，内容，域名，路径，有效时间等
# Chrome://settting/siteData---进行实验

from datetime import datetime
@blue.route('/login')
def login():
    b_name = session.get('login_user').get('b_name') #此处的session.get()获取的是设定session好的
    b_time=datetime.now()
    content=locals()
    response=make_response(render_template('login_success.html',**content),200)
    #添加/删除cookie,都是在响应对象中进行的
    response.set_cookie('wt','ja',expires=datetime.strptime('2021-09-19 10:20:00','%Y-%m-%d %H:%M:%S'))

    return response


# @blue.route('/find')
# def find():
#     #客户端的cookie信息随着请求发送，自动将浏览器中的cookie附加到请求头中
#     email=request.cookies.get('email') #value
#     return ''

#当多个session建立后，如何确定某个请求属于哪个session，这取决于
#cookie的信息，cookie中会存有session的ID

from model.user_login import UserModel
@blue.route('/login2',methods=['GET','POST'])
def login2():
    if request.method=='POST':
        name=request.form.get('name')
        password=request.form.get('password')
        if not all((name,password)):#验证是否为空
            message='cant be empty'
        else:
            #将数据写入数据库
            model=UserModel()
            #model.save(name=name,password=password)#注册时使用
            user=model.login(name,password)

            if not user:
                message="%s don't exist"%name
            else:
                session['login_user']=user

                return redirect('/login')
    money=10999881.28


    context = locals()  # 将本地变量的名和值包装成字典
    # for i ,j in context.items():
    #     print(i,j)
    # print((key,value)for (key ,value) in context )
    return render_template('login.html',**context)


@blue.route('/find_user',methods=['GET'])
def find_user():
    if not session.get('login_user'):
        return """当前没有登陆，请先<a href='/login2'>登陆</a>"""
    else:
        return redirect('/login')
    print('url',request.url)
    print('cookie',request.cookies)


#登出操作
@blue.route('/logout')
def logout():
    del session['login_user']
    return redirect('/login2')


@blue.route('/relate')
def relate():
    from model.user_login import Bank
    data={
        'all_bank':Bank.query.all()
    }
    return render_template('book.html',**data)





