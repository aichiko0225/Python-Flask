# -*- coding: utf-8 -*-
"""
    :author: ash
    :url: http://ashless.cc:3333
    :copyright: © 2020 ash
    :license: MIT, see LICENSE for more details.
"""
# from wtforms.form import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired, FileAllowed
# from flask_ckeditor import CKEditorField


# 4.2.1 basic form example
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


# custom validator
# class FortyTwoForm(FlaskForm):
#     answer = IntegerField('The Number')
#     submit = SubmitField()

#     def validate_answer(form, field):
#         if field.data != 42:
#             raise ValidationError('Must be 42.')
