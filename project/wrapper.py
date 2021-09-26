import datetime
from flask.globals import session
from .models import Item, ItemBlob, ItemComment, ItemLike, ItemPhoto, ItemTag, Tag, Univercity, User
from . import db

def user_save(user_name,univercity_name,email_address,password1,birthday,icon=None,db=db):
    univ=db.session.query(Univercity).filter_by(univercity_name=univercity_name).first()
    if univ is None:
        univ=Univercity(univercity_name=univercity_name)
        db.session.add(univ)
        # db.session.commit()
        db.session.flush()
    user_to_create = User(user_name=user_name,email_address=email_address,birthday=birthday,univercity_id=univ.id,icon=icon)
    user_to_create.password=password1
    db.session.add(user_to_create)
    db.session.commit()
    # db.session.rollback()
    
    return user_to_create

def item_save(item_name,user_id,expire_unix_time,place,state,message,handing_method,tags:list,itemphotos:list):
    try:
        expire_unix_time=int(expire_unix_time)
        # print(expire_unix_time)
        item=Item(item_name=item_name,user_id=user_id,expire=int(expire_unix_time),state=state,place=place,message=message,handing_method=handing_method)
        db.session.add(item)
        db.session.commit()
        item_id=item.id

        # add tag
        for t in tags:
            db.session.add(ItemTag(tag_name=t,item_id=item_id,created_at=int(datetime.datetime.now().timestamp())))
        # add photos
        for idx,photo in enumerate(itemphotos):
            if type(photo) != type("a"):
                blob=ItemBlob(blob=photo,item_id=item_id)
                db.session.add(blob)
                db.session.flush()
                db.session.add(ItemPhoto(item_id=item_id,photoNum=idx,URI="/items/blob/"+str(blob.id)))
            else:
                db.session.add(ItemPhoto(item_id=item_id,photoNum=idx,URI=photo))

        db.session.commit()
    except:
        import traceback
        db.session.rollback()
        traceback.print_exc()
        return False
    return item_id


# def item_like(item_id,user_id):
    # ItemLike()

def comment_save(item_id,user_id,comment):
    db.session.add(ItemComment(item_id=item_id,user_id=user_id,comment=comment))