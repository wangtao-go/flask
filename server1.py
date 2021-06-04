
##wsgi网关接口的make_server处理网络请求流程

from wsgiref.simple_server import make_server
import os




#处理业务最核心的函数
def app(env,make_response):

    # for k,v in env.items():
    #     print(k,':',v)
    headers=[]   #响应头，根据响应的数据增加不同的相应头k：v
    body=[]     #响应的数据
    path=env.get('PATH_INFO')#请求路径
    if path =='/favicon.ico':
        res_path=os.path.join('static','6.png')
        headers.append(('content-type','images/*'))
    elif path=='/':
        #主页
        res_path = os.path.join('static', 'h2.html')
        headers.append(('content-type', 'text/html;charset=utf-8'))
    else:
        #其它资源：css/js/pic/mp4/mp3
        res_path=os.path.join('static',path[1:])
        if res_path.endswith('.html'):
            headers.append(('content-type', 'text/html;charset=utf-8'))
        elif any((res_path.endswith('.png'),
                  res_path.endswith('.jpg '),
                  res_path.endswith('.gif'),)):
            headers.append(('content-type','images/*'))
        else:
            headers.append(('content-type','text/*;charset=utf-8'))

    #判断资源是否存在res_path
    status_code=200
    if not os.path.exists(res_path):
        status_code=404
        body.append('<h4 style="color:red">不存在</h4>'.encode())
    else:
        with open(res_path,'rb') as f:
            body.append(f.read())

    make_response('%s Ok'%status_code,headers)
    return body
    #响应头
    # make_response('200 OK',
    #               [('Content-Type','text/html;charset=utf-8')])
    # return ['<h3>Hi, WSGI</h3>'.encode('utf-8')] #响应数据

host='0.0.0.0'
port=8000
httpd=make_server(host,port,app)
print('running http://%s:%s' % (host,port))


#启动服务，开始监听客户端连接
httpd.serve_forever()










