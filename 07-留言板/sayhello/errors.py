# -*- coding: utf-8 -*-
"""
    :author: ash
    :url: http://ashless.cc:3333
    :copyright: © 2020 ash zhao <aichiko66@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

from flask import render_template

from sayhello import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
