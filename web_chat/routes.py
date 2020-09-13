from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user
from datetime import datetime

from web_chat import app, db
from web_chat.models import  Message, User


@app.route("/")
@app.route("/home")
@app.route("/main")
def main_page():
    '''Return main web-page '''
    return render_template("index.html")


@app.route('/sing-in',  methods=['GET','POST'])
def sing_in():
    '''Sing in to chat'''
    if request.method == 'GET':
        return render_template('sing-in.html')

    nickname=request.form.get('nickname')
    password=request.form.get('pass')

    if not nickname or not password:
        flash('Введите логин и пароль')
        return render_template('sing-in.html')

    if nickname and password:

        user = User.query.filter_by(nickname=nickname).first()
        if not user:
            flash("Такого пользователя нет в системе")
            return render_template('sing-in.html')

        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('get_contacts'))

        flash('Неправильно введен логин или пароль')
        return render_template('sing-in.html')

    return render_template('sing-in.html')


@app.route('/log-in', methods=['GET','POST'])
def login():
    '''Registration in chat'''
    if request.method == 'GET':
        return  render_template('log-in.html')

    nickname=request.form['nickname']
    password=request.form['pass']
    password_confirm=request.form['pass_confirm']

    #validation
    if not nickname or not password or not password_confirm:
        flash('Заполните все поля')
        return  render_template('log-in.html')

    if User.query.filter_by(nickname=nickname).first():
       flash('Пользователь с таким именем уже существует. Выберите другое.')
       return render_template('log-in.html')

    if password != password_confirm:
        flash('Пароли не совпадают')
        return render_template('log-in.html')

    password=generate_password_hash(password)
    user=User(nickname=nickname, password=password, register_time=datetime.now().timestamp())
    db.session.add(user)
    db.session.commit()
    user=User.query.filter_by(nickname=nickname).first()
    login_user(user)
    return redirect(url_for('get_contacts'))



@app.route('/log-out')
@login_required
def logout():
    '''Log out from chat'''
    logout_user()
    return redirect(url_for('main_page'))


@app.route('/contacts')
@login_required
def get_contacts():
    '''Return page with contacts which user can chat with'''
    user=User.query.filter_by(id=session['_user_id']).first()
    contacts=user.get_contacts()
    return render_template('contacts.html', nickname=user.nickname, contacts=contacts)


@app.route('/message-history/<username>', methods=['POST', 'GET'])
@login_required
def get_message_history(username):
    '''Return history of username and curreent user chating'''
    user = User.query.filter_by(id=session['_user_id']).first()
    if request.method == 'GET':
        messages=Message.get_messages(user.nickname, username)
        return render_template('messages.html', messages=''.join(message.to_string()+'\n' for message in messages), current_user=user.nickname, user=username)
    if request.form.get('message'):
        mes=Message(text=request.form.get('message'), from_nick=user.nickname, to_nick=username, sent_time=datetime.now().timestamp())
        db.session.add(mes)
        db.session.commit()
    return redirect(url_for('get_message_history', username=username))

@app.after_request
def redirect_to_sing_in(response):
    '''If somebody tries to get to some page without autorization, he is redirected to sing-in page'''
    try:
        if response.status_code == 401:
            return  redirect(url_for('sing_in'))
        return  response
    except:
        return response