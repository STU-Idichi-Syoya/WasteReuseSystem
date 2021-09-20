# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from .models import User,Univercity
from . import db
from .form import RegisterForm, LoginForm
from project.wrapper import user_save

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email_address=email).first()

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not user.check_password_correction(password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))

# @auth.route('/signup')
# def signup():
#     return render_template('signup.html')

# @auth.route('/signup', methods=['POST'])

@auth.route('/signup',methods=['GET','POST'])
@auth.route('/users/register',methods=['GET','POST'])
def signup():
    if request.method=='GET':
        form=RegisterForm()
        return render_template('signup.html',form=form)
    else:
        form = RegisterForm(request.form)
        if form.validate_on_submit():
            user_to_create = user_save(form.user_name.data,form.univercity_name.data,form.email_address.data,form.password1.data,form.birthday.data)
            login_user(user_to_create)
            flash(f'Account created successfuly! You are now logged as {user_to_create.user_name}', category='success')
            return redirect(url_for('main.profile'))
        if form.errors != {}:  # If there are not errors from the validations
            for err_msg in form.errors.values():
                flash(f'There was an error with creating a user: {err_msg}', category='danger')
                print(err_msg)
            return render_template('signup.html', form=form)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))