# -*- coding: utf-8 -*-
"""
    :author: ash
    :url: http://ashless.cc:3333
    :copyright: © 2020 ash zhao <aichiko66@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy


app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


from sayhello import views, errors, commands
