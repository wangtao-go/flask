import os

from flask import Blueprint, make_response, redirect, render_template, session
from flask import request

from model import db
from model.user_login import Books

blue = Blueprint('bookBlue', __name__)


@blue.route('', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get('author')
        name = request.form.get('book')
        type2 = request.form.get('type')
        publish_year = request.form.get('year')
        # id=request.form.get('id')
        if not all((author, name)):  # 有任何一个为空，all返回false，
            message = '作者的姓名不能为空'
        else:
            book = Books(author=author,
                         name=name,
                         type=type2,
                         publish_year=publish_year
                         )
            db.session.add(book)
            db.session.commit()
            success = '成功提交%s的书籍《%s》' % (author, name)
    book = Books.query.all()
    data = locals()
    return render_template('book.html', **data)


@blue.route('/book_del', methods=['GET', 'POST'])
def book_del():
    # 获取用户提交的要删除数据的id
    # pk = request.
    db.session.delete(Books.query.get())
    # 获取要删除的对象，删除
    # 重定向
    return redirect('/book')


#
@blue.route('/fictions', methods=['GET', 'POST'])
def fictions():
    fic_dir = os.listdir('/Users/wangtao/Desktop/flask1/apiserver/mainapp/static/fictions/我真的只有一个老婆')
    fic_dir.sort()
    t_list = []
    g = 0
    i = 0
    t_list2=[]
    while True:
        if i > len(fic_dir)-1:
            t_list2.append(t_list)
            break
        else:
            if i < 3 * g:
                t_list.append(fic_dir[i])
                i += 1
            else:
                t_list2.append(t_list)
                t_list=[]
                g += 1
                continue
    del t_list2[0]
    data = locals()
    return render_template('f_dir.html', **data)


#
@blue.route('/fictions_content/<int:book_id>', methods=['GET', 'POST'])
def fictions_dir(book_id):
    fic_dir = os.listdir('/Users/wangtao/Desktop/flask1/apiserver/mainapp/static/fictions/我真的只有一个老婆')
    fic_dir.sort()
    content_list = []
    for each in fic_dir:
        with open('/Users/wangtao/Desktop/flask1/apiserver/mainapp/static/fictions/我真的只有一个老婆/%s' % each,
                  'r+') as f:
            g = f.read()
            content_list.append(g)

    book_id = book_id
    last_page = book_id - 1
    next_page = book_id + 1
    data = locals()
    return render_template('f_content.html', **data)









