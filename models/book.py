#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from books import db


class Book(db.Document):
    bid = db.StringField(max_length=255, required=True)
    title = db.StringField(max_length=255, required=True)
    author = db.ListField(db.StringField(max_length=255), required=True)
    translator = db.ListField(db.StringField(max_length=255))
    img = db.URLField(required=True)
    url = db.URLField(required=True)
    summary = db.StringField()
    publisher = db.StringField()
    isbn = db.StringField(required=True)
    tags = db.ListField(db.ReferenceField('Tag'))
    add_time = db.DateTimeField(default=datetime.datetime.now, required=True)
    raters_num = db.IntField()
    rating_avg = db.StringField()
    meta = {
        'indexes': [
            {'fields': ['bid'], 'unique': True},
        ],
    }

    def __unicode__(self):
        return self.title


class Tag(db.Document):
    name = db.StringField(max_length=255, required=True)
    count = db.IntField(required=True, default=1)
    meta = {
        'indexes': [
            {'fields': ['name'], 'unique': True},
        ],
    }

    def __name__(self):
        return self.name
#Class Author(db.Document):

#class Resource(db.EmbeddedDocument):
    #resource_link =


#class Comment(db.EmbeddedDocumentj):
    #pass
