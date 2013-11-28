#!/usr/bin/env python
# -*- coding: utf-8 -*-

from books import db
import Book

class User(db.Document):
    name = db.StringField(max_length=255, required=True)
    password_hash = db.StringField(max_length=255, required=True)
