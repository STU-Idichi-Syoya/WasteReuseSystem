from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login.utils import expand_login_view
from flask_migrate import current
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required,current_user
from .models import Item, User
from . import db
from .form import ItemAdd
from project.wrapper import item_save

users_app = Blueprint('users', __name__)

# 検索画面
@users_app.route('/items/search' ,methods=['GET','POST'])
# @login_required
def search_page():
    
    return render_template('search.html')

@users_app.route('/items/add',methods=['GET','POST'])
@login_required
def item_add():
    if request.method=='GET':
        form=ItemAdd()
        return render_template('item_add.html',form=form)
    else:
        form=ItemAdd(request.form)
        if form.validate_on_submit():
            item_save(item_name=form.item_name.data,category=form.category.data,)
            return 'OK'
        return 'FALSE'