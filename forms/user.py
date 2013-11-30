#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.mongoengine.wtf import model_form
from models.user import User


UserForm = model_form(User)
