from project.wrapper import item_save
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required,current_user
from werkzeug.utils import send_file
from werkzeug.wrappers.response import Response
from .models import Item, ItemComment, ItemLike, ItemPhoto, ItemTag, Tag, TransactionComment, User,ItemBlob
from . import db
from .form import ItemAdd
from .util import get_tags
import io
items_app = Blueprint('items', __name__)

@items_app.route('/items/blob/<int:blob_id>')
def sendPhotoID(blob_id):
    blob=db.Query(ItemBlob).filter_by(id=blob_id)
    if blob is not None:
        return send_file(
            io.BytesIO(blob.blob),
            mimetype='image/jpeg',
            as_attachment=False,
        )
    return Response(status=400)

               

@items_app.route('/items/add',methods=['POST'])
def item_post():
    item_name=request.form['item_name']
    handing_method=request.form['handing_method']
    place=request.form['place']
    state=request.form['state']
    message=request.form['message']
    expire=request.form['expire']
    tags=get_tags(message)
    photos=request.files.getlist('photos')
    if len(photos)>5 or len(photos)<1:
        return 'Error Photo is too many'
    # TODO 縮小処理
    plist=[p.read()for p in photos]
    ret=item_save(item_name,current_user.user_id,expire,place,state,message,handing_method,tags,plist)
    if ret:
        return 'OK'
    else:
        return 'FALSE'
    
@items_app.route("/items/search")
def searchItems():
    tag=request.args.get('tag')
    keyword=request.args.get('keyword')


    
    # validation
    if tag is not None:
        tag=tag.replace(' ','')
    if keyword is not None:
        # 全角を半角にして、分割
        keyword=keyword.replace('　',' ').split(' ').replace(' ','')

    if len(tag)>0:
        #TODO:tag
        if current_user.is_authenticated:
            search_items=db.session.query(Item.id,Item.item_name,ItemPhoto.URI,ItemLike.is_like,Item.place,Item.user_id,Item.handing_method)\
                                            .join(ItemPhoto,ItemPhoto.item_id==Item.id)\
                                            .join(ItemTag,ItemTag.item_id==Item.id)\
                                            .join(Tag,Tag.id==ItemTag.tag_id)\
                                            .join(ItemLike,Item.id==ItemLike.item_id)\
                                            .join(User,Item.user_id==User.id)\
                                            .filter_by(is_like=True).filter_by(univercity_id==current_user.univercity_id,tag_name=tag).all()
            return render_template('search_result.html',search_items=searchItems)
            
        else:
            search_items=db.session.query(Item.id,Item.item_name,ItemPhoto.URI,ItemLike.is_like,Item.place,Item.user_id,Item.handing_method)\
                                        .join(ItemPhoto,ItemPhoto.item_id==Item.id)\
                                        .join(ItemTag,ItemTag.item_id==Item.id)\
                                        .join(Tag,Tag.id==ItemTag.tag_id)\
                                        .join(ItemLike,Item.id==ItemLike.item_id)\
                                        .join(User,Item.user_id==User.id)\
                                        .filter_by(is_like=True).filter_by(tag_name=tag).all()
            return render_template('search_result.html',search_items=searchItems)
    
    # find by keyword
    # TODO 複数ワード検索
    elif len(keyword)>0 and len(keyword[0])>0:
        if current_user.is_authenticated:
            search_items=db.session.query(Item.id,Item.item_name,ItemPhoto.URI,ItemLike.is_like,Item.place,Item.user_id,Item.handing_method)\
                                        .join(ItemPhoto,ItemPhoto.item_id==Item.id)\
                                        .join(ItemLike,Item.id==ItemLike.item_id)\
                                        .join(User,Item.user_id==User.id)\
                                        .filter_by(is_like=True).filter_by(univercity_id==current_user.univercity_id).all()
    
            return render_template('search_result.html',search_items=searchItems)
        else:
            search_items=db.session.query(Item.id,Item.item_name,ItemPhoto.URI,ItemLike.is_like,Item.place,Item.user_id,Item.handing_method)\
                                        .join(ItemPhoto,ItemPhoto.item_id==Item.id)\
                                        .join(ItemLike,Item.id==ItemLike.item_id)\
                                        .join(User,Item.user_id==User.id)\
                                        .filter_by(is_like=True).filter(Item.item_name.like(f'%{keyword[0]}%')).all()
            return render_template('search_result.html',search_items=search_items)
    # クエリパラメータがなければ、検索画面
    return render_template('search.html')

@items_app.route("/items/<id>")
def showItem(item_id):
    item=db.session.query(Item).filter_by(id=item_id).first()
    comment=db.session.query(ItemComment).filter_by(item_id=item_id).order_by(Item.created_at.amount.asc()).all()
    photos=db.session.query(ItemPhoto).filter_by(item_id=item_id).all()
    tag=db.session.query(ItemTag).join(Tag,Tag.id==ItemTag.tag_id).filter_by(item_id=item_id)
    if item is None:
        return f'ERROR {item_id} Item is not exist'
    return render_template('item_datail.html',item=item,comment=comment,photos=photos,tag=tag)


@items_app.route("/")
# @items_app.route("/items")
def showItems():
    #     User.idと、UserSocial.user_idで内部結合し、
    # ユーザ全てをList型で取得する。
    # user_nameはこの形式で取得される。
    # 返り値：[(User, UserSocial)]
    # user_name = session.query(User, UserSocial).\
    # join(UserSocial, User.id==UserSocial.user_id).\
    # all()
    if current_user.is_authenticated:
        # いいねしたアイテム
        like_items=db.session.query(Item.id,Item.item_name,ItemPhoto.URI,ItemLike.is_like)\
                                    .join(ItemPhoto,ItemPhoto.item_id==Item.id)\
                                    .join(ItemLike,Item.id==ItemLike.item_id)\
                                    .join(User,Item.user_id==User.id)\
                                    .filter_by(is_like=True).filter_by(univercity_id==current_user.univercity_id).limit(10).all()
        
        recommend_items=db.session.query(Item.id,Item.item_name,ItemPhoto.URI,ItemLike.is_like)\
                                    .join(ItemPhoto,ItemPhoto.item_id==Item.id)\
                                    .join(ItemLike,Item.id==ItemLike.item_id)\
                                    .join(User,Item.user_id==User.id)\
                                    .filter_by(univercity_id==current_user.univercity_id).limit(10).all()
        
        #検索履歴
        #TODO
        search_his_items=[]
        # new Item
        new_items=db.session.query(Item.id,Item.item_name,ItemPhoto.URI,ItemLike.is_like)\
                                    .join(ItemPhoto,ItemPhoto.item_id==Item.id)\
                                    .join(ItemLike,Item.id==ItemLike.item_id)\
                                    .join(User,Item.user_id==User.id)\
                                    .filter_by(univercity_id==current_user.univercity_id).limit(10).order_by(Item.created_at.amount.desc()).all()
        return render_template('index.html',like_items=like_items,recommend_items=recommend_items,new_items=new_items)
        
    else:
        recommend_items=db.session.query(Item.id,Item.item_name,ItemPhoto.URI,ItemLike.is_like)\
                                    .join(ItemPhoto,ItemPhoto.item_id==Item.id)\
                                    .join(ItemLike,Item.id==ItemLike.item_id)\
                                    .join(User,Item.user_id==User.id)\
                                    .limit(100).all()
        
        return render_template('index.html',recommend_items=recommend_items)

#取引コメントの表示とボタン
@items_app.route('/items/<item_id>/transaction')
def tsc_get(item_id):
    comments=db.session.query(TransactionComment).filter_by(item_id=id).order_by(ItemComment.created_at.amount.desc()).all()
    item=db.session.query(Item).filter_by(id=item_id).first()
    return render_template('transaction.html')

@items_app.route('/items/<item_id>/transaction/comments',methods=['POST'])
def tsc_get_c(item_id):
    comment=request.form['comment']
    item=db.session.query(Item).filter_by(id=item_id).first()
    db.session.add(TransactionComment(item_id=item_id,user_id=current_user.id,comment=comment))
    db.session.commit()
    return render_template('transaction.html')


# @items_app.route('/items/<item_id>/transaction/',methods=['DELETE'])
# def delete()