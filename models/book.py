#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from books import db


class Book(db.Document):
    _id = db.StringField(required=True)
    created_time = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(required=True)
