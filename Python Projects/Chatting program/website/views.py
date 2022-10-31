from flask import Blueprint, render_template,request
from flask_login import  login_required, current_user
from flask import Blueprint, render_template, request

views = Blueprint("views", __name__)

#Chatting page, using the chat html file
@views.route('/chatapp', methods=['GET','POST'])
@login_required
def chat():
    return render_template('chat.html', user=current_user)