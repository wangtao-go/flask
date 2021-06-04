from flask import Blueprint
from flask import request

blue=Blueprint('cardBlue',__name__)

@blue.route('/card',methods=['GET','POST'])
def card():
    return 'hellow wtao'


@blue.route('/add/<bankname>')
def addCard(bankname):
    return '%s success!'%bankname

from flask import url_for
@blue.route('/select_bank')
def selectbank():
    bankname='china bank'
    #next_url='/card/add/'+bankname
    return """
    sucess!3s later <a href='%s'>in</a>
    
    #以下用到了反向解析，通过寻址函数，给与参数，获得url
    """%url_for('cardBlue.addCard',bankname=bankname)





