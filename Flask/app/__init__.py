#!usr/bin/python
# -*- coding : utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app import falsk_2,model
