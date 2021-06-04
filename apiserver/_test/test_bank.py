import os

from flask import request
import requests
from unittest import TestCase


class TestBank(TestCase):
    # 测试单元测试的方法，以"test_"开头
    def test_del(self):
        url = 'http://localhost:5000/bank/del/100'
        method = 'DELETE'
        resp = requests.request(method, url)
        self.assertIs(resp.status_code, 200, 'failure')
        print(resp.text)

    def test_pulish(self):
        url = 'http://localhost:5000/bank/publish'
        method = 'post'
        resp = requests.post(url)
        self.assertEqual(resp.status_code, 200, '失败')
        print(resp.text)
        print(resp.headers.get('Content-Type'))


from mainapp import app
import settings
from model import db
from model.user_login import Bank, User, Card, Books


class TestUser(TestCase):

    def test_create(self):
        app.app_context().push()
        user = Bank(b_name='wang cong fa',
                    password=hash('0000'),
                    b_user_num='10'
                    )
        # user.b_name = 'hao_ing'
        # user.password = hash('anckzcn')
        db.session.add(user)
        db.session.commit()  # 通过session将数据提交到数据库

    def test_update(self):
        app.app_context().push()
        user = Bank.query.get(3)
        print(user)
        user.b_name = '.....'
        db.session.commit()  # 自动检测数据更新

    def test_delete(self):
        app.app_context().push()
        db.session.delete(Bank.query.get(5))
        db.session.commit()

    # 按照行的方式来读取数据，基于模型类发起查询，filter查询
    def test_filter(self):
        app.app_context().push()
        # filter本身是一个迭代器
        for u in Bank.query.filter(Bank.b_name == 'WT'):
            print(u)
        for u in Bank.query.filter(Bank.b_name.contains('w')):
            print(u)

    def test_filter_or_not(self):
        app.app_context().push()
        for bank in Bank.query.filter(
                db.or_(
                    Bank.b_id > 2,
                    Bank.b_name.like('%W%')
                )
        ):
            print(bank.b_name, bank.b_id)

    # 按照列的方式来读取数据,session查询

    def test_session_query(self):
        app.app_context().push()
        # session的query必须指定查询的模型
        u = db.session.query(Bank.b_id, Bank.b_name).all()
        print(u)
        print('------>')
        for i in u:
            print(i[0], i[1])
        print(type(u))

    # 排序和分页,默认升序排列ASC，可以指定降序排列DESC
    def test_model_order_page(self):
        app.app_context().push()
        for u in Bank.query.order_by(Bank.b_name, Bank.b_id.desc()).all():
            print(u.b_name)

        for u in Bank.query \
                .filter(Bank.b_name.contains('w')) \
                .order_by(Bank.b_id.desc()).all():
            print(u.b_name, u.b_id)

        # 分页 offset(),limit()

    def test_page(self):
        app.app_context().push()
        # total = Bank.query.count()
        # page_size = 2
        # pages = total // page_size + (1 if total % page_size > 0 else 0)
        # page = 2
        query_set = Bank.query.filter(db.or_(
            Bank.b_id > 2,
            Bank.b_id == 1
        )).order_by(Bank.b_id)
        print('------>')
        # print('total %s,current page %s,every page %s' % (pages, page, page_size))
        print('------>')
        for u in self.page_data(query_set, 1, 3).all():
            print(u.b_name, u.b_id)

        cnt = db.session.query(db.func.count(Bank.b_id)).first()
        print(cnt)
        # 可以将page_size,page,以及查询条件query_set作为关键字参数，放到函数中

    def page_data(self, query_set, page_size=2, page=2):
        app.app_context().push()
        total = query_set.count()
        pages = total // page_size + (1 if total % page_size > 0 else 0)
        print('total %s,current page %s,every page %s' % (pages, page, page_size))

        return query_set.offset((page - 1) * page_size).limit(page_size)


class TestRelationship(TestCase):
    def test_1(self):
        app.app_context().push()
        user = User.query.get(1)
        for card in user.cards:
            print(card.bank.b_name, card.money, card.number, card.user.username)


class TestBooks(TestCase):

    def test_book_create(self):
        app.app_context().push()
        book=Books(author='王小波',name='黄金时代',publish_year='1999-2-3',type='知青')
        # book = Books(author='w', name='x', type='b')
        db.session.add(book)
        db.session.commit()

    def test_fiction(self):
        app.app_context().push()
        fic_dir = os.listdir('/Users/wangtao/Desktop/flask1/apiserver/mainapp/static/fictions/我真的只有一个老婆')
        g_list = []
        for each in fic_dir:
            with open('/Users/wangtao/Desktop/flask1/apiserver/mainapp/static/fictions/我真的只有一个老婆/%s' % each,
                      'r+') as f:
                g = f.read()
                g_list.append(g)

        # print(g_list)
        data = locals()
        print('------>>>>>>>')
        # print(data)

    def test_fictions(self):
        fic_dir = os.listdir('/Users/wangtao/Desktop/flask1/apiserver/mainapp/static/fictions/我真的只有一个老婆')
        fic_dir.sort()
        t_list = []
        g = 0
        i = 0
        t_list2 = []
        while True:
            if i > len(fic_dir) - 1:

                break
            else:
                if i < 3 * g:
                    t_list.append(fic_dir[i])
                    i += 1
                else:
                    t_list2.append(t_list)
                    t_list = []
                    g += 1
                    continue
        del t_list2[0]
        data = locals()
        for i in t_list2:
            print(i)
            print(type(i))
            print(fic_dir.index(i[0]))
            print('<<<>>>>')
        # print(data)
        print('-------->')
        # return render_template('f_dir.html', **data)















