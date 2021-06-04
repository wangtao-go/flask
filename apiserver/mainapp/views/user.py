from flask import Blueprint, render_template
from flask import request

blue=Blueprint('userBlue',__name__)

@blue.route('/',methods=['GET','POST'])
def user():
    return render_template('index.html')








