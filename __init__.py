#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

from books.views import book
app.register_blueprint(book.bp)

if __name__ == '__main__':
    app.run()
