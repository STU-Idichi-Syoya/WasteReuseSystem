from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login.utils import expand_login_view
from flask_migrate import current
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required,current_user
from werkzeug.utils import send_file
from werkzeug.wrappers.response import Response
from .models import Item, User,ItemBlob
from . import db
from .form import ItemAdd
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
