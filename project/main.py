# main.py

from .models import User
from . import db
from .wrapper import comment_save, item_save, user_save
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .util import get_tags

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/users/me')
@login_required
def profile():
    return render_template('mypage.html', name=current_user.user_name)

import csv

@main.route("/seed-user")
def seed():
    with open(r"DB_sample_user.csv",encoding="utf8") as user:
        f=csv.DictReader(user)
        for i,u in enumerate(f):
            user_save(u["ユーザー名"],"東京美術大学", f"{i}@tokyo-art.ac.jp", "password1", 100000,icon="/user/"+u["image"])
    return 'OK'

import datetime
@main.route("/seed-items")
def seed_items():
    
    with open(r"DB_sample_item.csv",encoding="utf8") as f:
        f=csv.DictReader(f)
        for i,item in enumerate(f):
            if item["is_enable"]=="FALSE":continue
            # print(item)
            user=db.session.query(User.id).filter_by(user_name=item["投稿者"]).first()
            user=user[0]
            date = datetime.datetime.strptime(item["有効期限"], '%Y/%m/%d').timestamp()
            tags=get_tags(item["アイテムの説明"])
            item_id=item_save(item_name=item['アイテム名'],user_id=user,expire_unix_time=date,place=item["テキスト"],state="傷少しあります",message=item["アイテムの説明"]
            ,handing_method=item["受け渡し方法"],tags=tags,itemphotos=["/images/item/"+item["アイテムの画像"]])

            for j in range(1,4):
                if not item["ユーザ名"+str(j)] :break
                user,user_name=db.session.query(User.id,User.user_name).filter_by(user_name=item["ユーザ名"+str(j)]).first()
                if user_name == "": break
                comment_save(item_id,user,item[f"コメント{j}"])
    return 'OK'
                