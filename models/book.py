#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from books import db


class Book(db.Document):
    book_id = db.StringField(required=True)
    book_title = db.StringField(required=True)
    book_author =
    book_translator =
    book_img =
    book_url =
    book_summary =
    book_publisher =
    book_isbn =
    book_tags = ListField()
    book_add_time = db.DateTimeField(default=datetime.datetime.now, required=True)

class Tag(db.EmbeddedDocument):
    tag_name =
    tag_title =
    tag_count =

class Resource(db.EmbeddedDocument):
