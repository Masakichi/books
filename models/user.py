#!/usr/bin/env python
# -*- coding: utf-8 -*-

from books import db


class User(db.Document):
    uid = db.IntField(required=True)
    name = db.StringField(max_length=255, required=True)
    password_hash = db.StringField(max_length=255, required=True)
    email = db.EmailField()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.name)
