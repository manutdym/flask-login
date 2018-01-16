#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import  Required
from flask_wtf import FlaskForm

#登录表单
class Login_Form(FlaskForm):
    name=StringField('name',validators=[Required()])
    pwd=PasswordField('pwd',validators=[Required()])

    submit=SubmitField('Login in')


#注册表单
class Register_Form(FlaskForm):
    name=StringField('name',validators=[Required()])
    pwd=PasswordField('pwd',validators=[Required()])
    submit=SubmitField('register')