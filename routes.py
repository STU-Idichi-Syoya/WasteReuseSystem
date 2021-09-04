from flask import render_template, redirect, url_for, flash, request,Flask,Response,abort
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from db.model import session
import db.wrapper as db

app=Flask(__name__)
app.config['SECRET_KEY'] = "secret"

login_maneger=LoginManager(app=app)

@app.teardown_request
def remove_session(ex=None):
    session.remove()

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/items/search' ,methods=['GET','POST'])
@login_required
def market_page():
    return render_template('search.html')

@app.route('/items/new', methods=['GET', 'POST'])
@login_required
def register_page():
    return render_template('new.html')

@app.route('/login', methods=['GET', 'POST'])
@app.route('/users/login', methods=['GET', 'POST'])
def login_page():
    if request.method=='GET':
        return render_template('login.html')
    elif request.method=='POST':
        mailadr=request.form['mailAddr']
        passwd=request.form['passwd']
        user=db.FindUserByMailAddrPasswd(mailadr,passwd)
        if user==None:
            abort(Response('userNotFound',status=401))
        else:
            login_user(user)
            return Response('login okay')
    
@app.route('/users/new')
def regist_new_User():
    return render_template()

@app.route('/users/logout')
def logout_page():
    logout_user()
    return Response('okay')


@login_maneger.user_loader
def usrLoder(usrId):
    db.findByUserId(int(usrId))

def RunApp():
    app.run(debug=True)
