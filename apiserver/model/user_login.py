import hashlib

from model import BaseModel
def hash(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

class UserModel(BaseModel):
    def login(self,name,password):
        #super是指的父类，此处为父类的重写
        pwd=hash(password)
        result=super().find_all('bank',' where b_name=%s and password=%s',name,pwd)
        if not result:
            return False
        else:
            return result[0]

    def save(self,**data):
        data['password']=hash(data['password'])
        return super().save('bank',**data)

##对父类进行重写
    def update(self,**data):
        if not data.get('b_id'):
            return False
        b_id=data.pop('b_id')

        if data.get('password'):
            data['password'] = hash(data['password'])

        return super().update('bank',b_id,**data)



from model import db
class Bank(db.Model):
    #声明字段（属性），默认情况下属性名与字段相同
    #b_id=db.column(db.Integer,primary_key=True,autoincrement=True,nullnable=False)
    b_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    b_name=db.Column(db.String(20))
    b_user_num=db.Column(db.Integer)
    password=db.Column(db.String(254))
    def __str__(self):
        return '%s %s'%(self.b_name,self.b_id)
    #__str__,将对象地址返回为要返回的字符串


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(20),unique=True)
    bank=db.Column(db.String(20))
    card_num=db.Column(db.Integer)


class Card(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    number=db.Column(db.String(20),unique=True)
    money=db.Column(db.Float(2),default=0,server_default='0')
    passwd=db.Column(db.String(100))
    # user_id=db.Column(db.String(20))
    # bank_id=db.Column(db.Integer)
    #
    # @property
    # def user_id(self):
    #     return Bank.query.filter(Bank.b_id==self.id).all()[0].password
    #     #return 'hahah'
    #模型的关系建立在多端
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    user=db.relationship(User,backref='cards') #反向关联，两个模型之间的关系确立，必须存在一个外键约束
    bank_id = db.Column(db.Integer, db.ForeignKey('bank.b_id'))
    bank = db.relationship(Bank, backref='cards')


class Books(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    author=db.Column(db.String(255))
    type=db.Column(db.String(255))
    name=db.Column(db.String(255))
    publish_year=db.Column(db.Date)







#
if __name__ == '__main__':
    user=UserModel()
    # ---------login-----------#
    r=user.login('WT','12345')
    print(r)

#     # ---------save-----------#
#     # r=dict(b_id=1004,b_name='hui',b_user_num=5,password='2021')
#     # result=user.save(**r)
#     # print(result)
#     # ---------update-----------#
#     update_user=dict(b_id=1002,b_name='ren')
#     print(user.update(**update_user))








