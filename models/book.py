#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from books import db


class Book(db.Document):
    bid = db.StringField(required=True)
    title = db.StringField(required=True)
    author = db.ListField()
    translator = db.ListField()
    img = db.URLField()
    url = db.URLField()
    summary = db.StringField()
    publisher = db.StringField()
    isbn = db.StringField()
    tags = db.ListField(db.ReferenceField('Tag'))
    add_time = db.DateTimeField(default=datetime.datetime.now, required=True)
    raters_num = db.IntField()
    rating_avg = db.StringField()

    def __unicode__(self):
        return self.title


class Tag(db.Document):
    name = db.StringField()
    count = db.IntField()

    def __unicode__(self):
        return self.name


#Class Author(db.Document):

#class Resource(db.EmbeddedDocument):
    #resource_link =


#class Comment(db.EmbeddedDocumentj):
    #pass
