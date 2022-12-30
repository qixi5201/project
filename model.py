from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask import Flask
from datetime import datetime


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:rootroot@localhost:3306/測試"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
Migrate(app,db)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    head=db.Column(db.String(64))
    main=db.Column(db.String(64))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    tag=db.Column(db.String(64))

    def __init__(self, head, main, body,timestamp,tag):
        self.head = head
        self.main =main
        self.body = body
        self.timestamp=timestamp
        self.tag=tag

