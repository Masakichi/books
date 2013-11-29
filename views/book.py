#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, url_for
from books.models.book import Book
from books.api.douban import add_book


bp = Blueprint('book', __name__)


@bp.route('/')
def index():
    #return 'hello.'
    books = Book.objects.all()
    return render_template('index.html', books=books)


@bp.route('/add/<bid>')
def add(bid):
    add_book(bid)
    return 'add book success'


@bp.route('/show/<bid>')
def show(bid):
    book = Book.objects.get_or_404(bid=bid)
    return book.title
