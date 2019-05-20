import json
from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# 模块管理
from app import mkdirs_sql,models #数据库管理模块
from app.api import test_sql,routes 


