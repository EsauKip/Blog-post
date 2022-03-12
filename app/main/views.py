from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import UpdateProfile
from .. import db,photos
from ..requests import get_quote
from flask_login import current_user, login_required
from ..models import User, Blog, Comment,Subscriber
from app.main.forms import BlogForm,CommentForm
from datetime import datetime

@main.route("/", methods=["GET", "BLOG"])
def index():
    blogs = Blog.get_all_blogs()
    quote = get_quote()

    return render_template("index.html", blogs=blogs, quote=quote)
