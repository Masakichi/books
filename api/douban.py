#!/usr/bin/env python
# -*- coding: utf-8 -*-

from books.models.book import Book
import requests


def add_book(bid):
    book_raw = requests.get('https://api.douban.com/v2/book/%s' % bid)
    book_dict = book_raw.json()
    bid = book_dict['id']
    title = book_dict['title']
    author = book_dict['author']
    translator = book_dict['translator']
    img = book_dict['image']
    url = book_dict['url']
    summary = book_dict['summary']
    publisher = book_dict['publisher']
    isbn = book_dict['isbn13']
    tags = book_dict['tags']
    tag_list = []
    for tag in tags:
        tag_list.append(tag['name'])

    tags = tag_list
    raters_num = book_dict['rating']['numRaters']
    rating_avg = book_dict['rating']['average']

    book = Book(
        bid=bid,
        title=title,
        author=author,
        translator=translator,
        img=img,
        url=url,
        summary=summary,
        publisher=publisher,
        isbn=isbn,
        tags=tags,
        raters_num=raters_num,
        rating_avg=rating_avg
    )

    book.save()
