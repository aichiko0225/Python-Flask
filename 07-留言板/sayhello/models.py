# -*- coding: utf-8 -*-
"""
    :author: ash
    :url: http://ashless.cc:3333
    :copyright: © 2020 ash zhao <aichiko66@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

from datetime import datetime
from sayhello import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)
