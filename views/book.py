#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint

bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    return 'hello.'


@bp.route('/<bid>')
def show_book_detail(bid):
    return 'Book %s' % bid
