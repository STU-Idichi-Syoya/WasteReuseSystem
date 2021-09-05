from flask import render_template, redirect, url_for, flash, request,Flask,Response,abort ,session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user,UserMixin
from waste.forms import RegisterForm, LoginForm
from waste.model import Item, User
from . import wrapper
from waste import db, login_manager,app

@app.teardown_request
def remove_session(ex=None):
    #session.removeじゃなくてclearじゃないのか？
    session.remove()

# ホーム画面
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# 検索画面
@app.route('/items/search' ,methods=['GET','POST'])
@login_required
def search_page():
    return render_template('search.html')

# 出品画面
@app.route('/items/add', methods=['GET', 'POST'])
@login_required
def add_page():
    return render_template('add.html')

# ログイン画面
@app.route('/login', methods=['GET', 'POST'])
@app.route('/users/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if request.method=='GET':
        return render_template('login.html', form=form)
    elif request.method=='POST':
        mailadr=form.user_name.data
        passwd=form.password.data
        attempted_user = wrapper.FindUserByMailAddrPasswd(mailadr, passwd)
        print(wrapper.findAll()[0].email_address)
        print(wrapper.findAll()[0].password_hash)
        if attempted_user==None:
            abort(Response('userNotFound', status=401))

        else:
            login_user(attempted_user)
            flash(f'ログイン成功! {attempted_user.username}さん', category='success')
            return redirect(url_for('add_page'))
    
# 会員登録画面
@app.route('/users/register')
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,email_address=form.email_address.data,password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfuly! You are now logged as {user_to_create.username}', category='success')

        return redirect(url_for('market_page'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

# ログアウト
@app.route('/users/logout')
def logout_page():
    logout_user()
    flash("ログアウト成功", category="info")
    return redirect(url_for("home_page"))

@app.route('/items/search',methods=['POST','GET'])
def search():
    if request.method=='GET':
        render_template('items-search.html')
    elif request.method=='POST':
        searchWord=request.form['searchWord']
        if len(searchWord.replace(' ','').replace('\t',''))==0:
                render_template('items-search.html')
        items=wrapper.findItemByWord(searchWord,userId=current_user.id)
        render_template('items-search-result.html',items=items)

@login_manager.user_loader
def usrLoder(usrId):
    wrapper.findByUserId(int(usrId))


