#!/usr/bin/env python
# -*- coding: utf-8 -*-

from settings import app

#views
@app.route('/')
def index():
    pass

@app.route('/book/<int:book_id>')
def book():
    pass

@app.route('/top')
def top():
    pass

@app.route('/tags')
def tags():
    pass

#run
app.run()
