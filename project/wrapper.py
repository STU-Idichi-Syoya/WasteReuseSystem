from flask.globals import session
from .models import Item, ItemBlob, ItemLike, ItemPhoto, ItemTag, Tag, Univercity, User
from . import db

def user_save(user_name,univercity_name,email_address,password1,birthday,db=db):
    univ=db.session.query(Univercity).filter_by(univercity_name=univercity_name).first()
    if univ is None:
        univ=Univercity(univercity_name=univercity_name)
        db.session.add(univ)
        # db.session.commit()
        db.session.flush()
    user_to_create = User(user_name=user_name,email_address=email_address,birthday=birthday,univercity_id=univ.id)
    user_to_create.password=password1
    db.session.add(user_to_create)
    db.session.commit()
    # db.session.rollback()
    
    return user_to_create

def item_save(item_name,user_id,expire_unix_time,place,state,message,handing_method,item_desc,tags:list,itemphotos:list):
    try:
        item=Item(item_name,user_id=user_id,expire=expire_unix_time,state=state,message=message,handing_method=handing_method)
        db.session.add(item)
        db.session.flush()
        item_id=item.id

        # add tag
        for t in tags:
            tag_id=db.session.query(Tag.id).filter_by(tag_name=t)
            if tag_id is None:
                db.session.add(Tag(tag_name=t))
                db.session.flush()
            db.session.add(ItemTag(tag_id=tag_id,item_id=item_id))
        # add photos
        for idx,photo in enumerate(itemphotos):
            blob=ItemBlob(blob=photo,item_id=item_id)
            db.session.add(blob)
            db.session.flush()
            db.session.add(ItemPhoto(item_id=item_id,photoNum=idx,URI="/items/blob/"+str(blob.id)))
        db.session.commit()
    except:
        db.session.rollback()
        return False
    return True


def item_like(item_id,user_id):
    ItemLike()