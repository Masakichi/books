#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Blueprint, render_template, url_for
from books.models.user import User

@login_manager.user_loader
def load_user(userid):
    return User.objects.get(uid=int(userid))

bp = Blueprint('user', __name__)


@bp.route('/')
def index():
    #return 'hello.'
    books = Book.objects.all()
    return render_template('index.html', books=books)
