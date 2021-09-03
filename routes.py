from flask import render_template, redirect, url_for, flash, request

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/items/search' ,methods=['GET','POST'])
@login_required
def market_page():

    return render_template('search.html')


@app.route('/items/new', methods=['GET', 'POST'])
def register_page():

    return render_template('new.html')

@app.route('/users/login', methods=['GET', 'POST'])
def login_page():
            
    return render_template('login.html')
    

@app.route('/users/new')
def logout_page():

    return render_template()
