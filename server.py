from flask import Flask, request, url_for, redirect, render_template,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from form import PostForm,RegisterForm,LoginForm,MessagesForm,SuggestForm
from flask_bootstrap import Bootstrap
from datetime import datetime
from  sqlalchemy.sql.expression import func

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:rootroot@localhost:3306/p"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
Migrate(app,db)
Bootstrap(app)
db.init_app(app)

class UserReister(db.Model):
    __tablename__ = 'UserReister'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return 'username:%s, email:%s' % (self.userid, self.email)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    head=db.Column(db.String(64))
    main=db.Column(db.String(64))
    body = db.Column(db.Text)
    timestamp = db.Column(db.Date, index=True, default=datetime.date)
    tag=db.Column(db.String(64))
    author = db.Column(db.String(80), db.ForeignKey('UserReister.userid'))
    like=db.Column(db.Integer)

    def __init__(self, head, main, body,timestamp,tag,author,like):
        self.head = head
        self.main =main
        self.body = body
        self.timestamp=timestamp
        self.tag=tag
        self.author=author
        self.like=like

class Save(db.Model):
    __tablename__ = 'saves'
    id = db.Column(db.Integer, primary_key=True)
    head=db.Column(db.String(64))
    main=db.Column(db.String(64))
    body = db.Column(db.Text)
    timestamp = db.Column(db.Date, index=True, default=datetime.date)
    tag=db.Column(db.String(64))
    author = db.Column(db.String(80), db.ForeignKey('UserReister.userid'))

    def __init__(self, head, main, body,timestamp,tag,author):
        self.head = head
        self.main =main
        self.body = body
        self.timestamp=timestamp
        self.tag=tag
        self.author=author
        
class Message(db.Model):
     id = db.Column(db.Integer,primary_key=True)
     name = db.Column(db.String(30))
     body = db.Column(db.String(100))
     timestamp = db.Column(db.DateTime, default=datetime.now,index=True)
     postid=db.Column(db.Integer)

class collect(db.Model):
     id = db.Column(db.Integer,primary_key=True)
     postid=db.Column(db.Integer, db.ForeignKey('posts.id'))
     author = db.Column(db.String(80), db.ForeignKey('UserReister.userid'))


class like(db.Model):
     id = db.Column(db.Integer,primary_key=True)
     postid=db.Column(db.Integer, db.ForeignKey('posts.id'))
     author = db.Column(db.String(80), db.ForeignKey('UserReister.userid'))

class Suggest(db.Model):
     id = db.Column(db.Integer,primary_key=True)
     name = db.Column(db.String(30))
     body = db.Column(db.String(100))
     email=db.Column(db.String(80))
     timestamp = db.Column(db.DateTime, default=datetime.now,index=True)

class Spot(db.Model):
    __tablename__ = 'spot'
    id = db.Column(db.Integer, primary_key=True)
    head=db.Column(db.String(100))
    main=db.Column(db.String(100))
    pic=db.Column(db.String(100))
    tag=db.Column(db.String(64))
    url=db.Column(db.String(64))

app.secret_key = "supersecretassuperx"
app.permanent_session_lifetime = timedelta(minutes=10)

@app.route('/')
def index():
     likes1=Post.query.order_by(Post.like.desc()).limit(10)
     a1=[]
     a2=[]
     for item in likes1:
          a1.append(item.head)
          a2.append(item.like)
     return render_template("??????.html",values=Post.query.order_by(Post.id.desc()).limit(6),form = SuggestForm(),values1=Spot.query.order_by(func.rand()).limit(3),likes1=likes1,a1=a1,a2=a2)
@app.route('/viewuser_<userid>', methods=['post', 'get'])
def viewuser(userid):
     return render_template("????????????.html",userid=userid,values1=Post.query.filter_by(author=userid).all(),values2=Post.query.filter(collect.author==userid,Post.id==collect.postid).all(),values3=Post.query.filter(like.author==userid,Post.id==like.postid).all())

@app.route('/allspot', methods=['GET'])
def spot():
     if request.method == 'POST':
        return redirect(url_for('??????.html'))

     return render_template('??????.html')

#??????????????????
@app.route('/spot1', methods=['GET'])
def areaone():
     if request.method == 'POST':
        return redirect(url_for('??????.html'))

     return render_template('????????????.html')

@app.route('/spot2', methods=['GET'])
def areatwo():
     if request.method == 'POST':
        return redirect(url_for('??????.html'))

     return render_template('????????????.html')

@app.route('/userspot1', methods=['GET'])
def userspot1():
     if request.method == 'POST':
        return redirect(url_for('??????.html'))
     return render_template('??????????????????.html',values=Post.query.filter_by(tag='??????').all())

@app.route('/userspot2', methods=['GET'])
def userspot2():
     if request.method == 'POST':
        return redirect(url_for('??????.html'))

     return render_template('??????????????????.html',values=Post.query.filter_by(tag='??????').all())

@app.route('/spot3', methods=['GET'])
def areathree():
     if request.method == 'POST':
        return redirect(url_for('??????.html'))

     return render_template('?????????.html')

@app.route('/spot4', methods=['GET'])
def areafour():
     if request.method == 'POST':
        return redirect(url_for('??????.html'))

     return render_template('??????.html')

@app.route('/spot5', methods=['GET'])
def areafive():
     if request.method == 'POST':
        return redirect(url_for('??????.html'))

     return render_template('??????.html')

#??????????????????
@app.route('/spot1_1', methods=['GET','POST'])
def spot1_1():
     postid=1
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_2', methods=['GET','POST'])
def spot1_2():
     postid=2
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
        if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_3', methods=['GET','POST'])
def spot1_3():
     postid=3
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_4', methods=['GET','POST'])
def spot1_4():
     postid=4
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_5', methods=['GET','POST'])
def spot1_5():
     postid=5
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_6', methods=['GET','POST'])
def spot1_6():
     postid=6
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????????.html',form=MessagesForm(),messages=messages)  
     return render_template('??????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_7', methods=['GET','POST'])
def spot1_7():
     postid=7
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????-???????????? .html',form=MessagesForm(),messages=messages)
     return render_template('????????????-???????????? .html',form=MessagesForm(),messages=messages)

@app.route('/spot1_8', methods=['GET','POST'])
def spot1_8():
     postid=8
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????? ??????????????? .html',form=MessagesForm(),messages=messages)
     return render_template('??????????????? ??????????????? .html',form=MessagesForm(),messages=messages)

@app.route('/spot1_9', methods=['GET','POST'])
def spot1_9():
     postid=9
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????????????? .html',form=MessagesForm(),messages=messages)
     return render_template('?????????????????? .html',form=MessagesForm(),messages=messages)

@app.route('/spot1_10', methods=['GET','POST'])
def spot1_10():
     postid=10
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????&?????????&????????? .html',form=MessagesForm(),messages=messages)
     return render_template('????????????&?????????&????????? .html',form=MessagesForm(),messages=messages)

@app.route('/spot1_11', methods=['GET','POST'])
def spot1_11():
     postid=11
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_12', methods=['GET','POST'])
def spot1_12():
     postid=12
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('??????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_13', methods=['GET','POST'])
def spot1_13():
     postid=13
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('??????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_14', methods=['GET','POST'])
def spot1_14():
     postid=14
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_15', methods=['GET','POST'])
def spot1_15():
     postid=15
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????? ArtBox.html',form=MessagesForm(),messages=messages)
     return render_template('???????????? ArtBox.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_16', methods=['GET','POST'])
def spot1_16():
     postid=16
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('??????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_17', methods=['GET','POST'])
def spot1_17():
     postid=17
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????MIRANEW SQUARE.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????MIRANEW SQUARE.html',form=MessagesForm(),messages=messages)

@app.route('/spot1_18', methods=['GET','POST'])
def spot1_18():
     postid=18
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

#??????????????????
@app.route('/spot2_1', methods=['GET','POST'])
def spot2_1():
     postid=19
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_2', methods=['GET','POST'])
def spot2_2():
     postid=20
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_3', methods=['GET','POST'])
def spot2_3():
     postid=21
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('??????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_4', methods=['GET','POST'])
def spot2_4():
     postid=22
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('??????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_5', methods=['GET','POST'])
def spot2_5():
     postid=23
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????????????????????????????????????????(?????????).html',form=MessagesForm(),messages=messages)
     return render_template('????????????????????????????????????????????????(?????????).html',form=MessagesForm(),messages=messages)

@app.route('/spot2_6', methods=['GET','POST'])
def spot2_6():
     postid=24
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_7', methods=['GET','POST'])
def spot2_7():
     postid=25
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????&??????&???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????&??????&???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_8', methods=['GET','POST'])
def spot2_8():
     postid=26
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('??????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_9', methods=['GET','POST'])
def spot2_9():
     postid=27
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_10', methods=['GET','POST'])
def spot2_10():
     postid=28
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????&??????????????????3D??????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????&??????????????????3D??????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_11', methods=['GET','POST'])
def spot2_11():
     postid=29
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_12', methods=['GET','POST'])
def spot2_12():
     postid=30
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_13', methods=['GET','POST'])
def spot2_13():
     postid=31
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('??????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_14', methods=['GET','POST'])
def spot2_14():
     postid=32
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('??????????????????.html',form=MessagesForm(),messages=messages)
     
@app.route('/spot2_15', methods=['GET','POST'])
def spot2_15():
     postid=33
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????????????????).html',form=MessagesForm(),messages=messages)
     return render_template('????????????????????????).html',form=MessagesForm(),messages=messages)

@app.route('/spot2_16', methods=['GET','POST'])
def spot2_16():
     postid=34
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot2_17', methods=['GET','POST'])
def spot2_17():
     postid=35
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)

#???????????????
@app.route('/spot3_1', methods=['GET','POST'])
def spot3_1():
     postid=36
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('Uncle Duncan.html',form=MessagesForm(),messages=messages)
     return render_template('Uncle Duncan.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_2', methods=['GET','POST'])
def spot3_2():
     postid=37
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_3', methods=['GET','POST'])
def spot3_3():
     postid=38
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('Binma Area 134.html',form=MessagesForm(),messages=messages)
     return render_template('Binma Area 134.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_4', methods=['GET','POST'])
def spot3_4():
     postid=39
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????Rc1899 Caf??.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????Rc1899 Caf??.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_5', methods=['GET','POST'])
def spot3_5():
     postid=40
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('Ancre caf?????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('Ancre caf?????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_6', methods=['GET','POST'])
def spot3_6():
     postid=41
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_7', methods=['GET','POST'])
def spot3_7():
     postid=42
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_8', methods=['GET','POST'])
def spot3_8():
     postid=43
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('?????????????????????.html',form=MessagesForm(),messages=messages )

@app.route('/spot3_9', methods=['GET','POST'])
def spot3_9():
     postid=44
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????????caf??.html',form=MessagesForm(),messages=messages)
     return render_template('??????????????????caf??.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_10', methods=['GET','POST'])
def spot3_10():
     postid=45
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????Mydeli???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('??????Mydeli???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_11', methods=['GET','POST'])
def spot3_11():
     postid=46
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_12', methods=['GET','POST'])
def spot3_12():
     postid=47
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????.html',form=MessagesForm(),messages=messages)
     return render_template('??????.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_13', methods=['GET','POST'])
def spot3_13():
     postid=48
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_14', methods=['GET','POST'])
def spot3_14():
     postid=49
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????(???????????????) .html',form=MessagesForm(),messages=messages)
     return render_template('???????????????(???????????????) .html',form=MessagesForm(),messages=messages)

@app.route('/spot3_15', methods=['GET','POST'])
def spot3_15():
     postid=50
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_16', methods=['GET','POST'])
def spot3_16():
     postid=51
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????Britshake??????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????Britshake??????.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_17', methods=['GET','POST'])
def spot3_17():
     postid=52
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('P Cafe.html',form=MessagesForm(),messages=messages)
     return render_template('P Cafe.html',form=MessagesForm(),messages=messages)

@app.route('/spot3_18', methods=['GET','POST'])
def spot3_18():
     postid=53
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('Handshop ?????????(?????????).html',form=MessagesForm(),messages=messages)
     return render_template('Handshop ?????????(?????????).html',form=MessagesForm(),messages=messages)

#????????????
@app.route('/spot4_1', methods=['GET','POST'])
def spot4_1():
     postid=54
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_2', methods=['GET','POST'])
def spot4_2():
     postid=55
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_3', methods=['GET','POST'])
def spot4_3():
     postid=56
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_4', methods=['GET','POST'])
def spot4_4():
     postid=57
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('La Villa Danshui.html',form=MessagesForm(),messages=messages)
     return render_template('La Villa Danshui.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_5', methods=['GET','POST'])
def spot4_5():
     postid=58
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????BALI ????????????-?????????.html',form=MessagesForm(),messages=messages)
     return render_template('??????BALI ????????????-?????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_6', methods=['GET','POST'])
def spot4_6():
     postid=59
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('Pescador Cafe ????????????.html',form=MessagesForm(),messages=messages)
     return render_template('Pescador Cafe ????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_7', methods=['GET','POST'])
def spot4_7():
     postid=60
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_8', methods=['GET','POST'])
def spot4_8():
     postid=61
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????.html',form=MessagesForm(),messages=messages)
     return render_template('?????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_9', methods=['GET','POST'])
def spot4_9():
     postid=62
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_10', methods=['GET','POST'])
def spot4_10():
     postid=63
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('MiNi??????.html',form=MessagesForm(),messages=messages)
     return render_template('MiNi??????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_11', methods=['GET','POST'])
def spot4_11():
     postid=64
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???Bar ?????????.html',form=MessagesForm(),messages=messages)
     return render_template('???Bar ?????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_12', methods=['GET','POST'])
def spot4_12():
     postid=65
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_13', methods=['GET','POST'])
def spot4_13():
     postid=66
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_14', methods=['GET','POST'])
def spot4_14():
     postid=67
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('Pallet Bistro??????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('Pallet Bistro??????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_15', methods=['GET','POST'])
def spot4_15():
     postid=68
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('Number 7 ????????????.html',form=MessagesForm(),messages=messages)
     return render_template('Number 7 ????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_16', methods=['GET','POST'])
def spot4_16():
     postid=69
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????? Hoshizuki.html',form=MessagesForm(),messages=messages)
     return render_template('?????? Hoshizuki.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_17', methods=['GET','POST'])
def spot4_17():
     postid=70
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_18', methods=['GET','POST'])
def spot4_18():
     postid=71
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_19', methods=['GET','POST'])
def spot4_19():
     postid=72
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('DAPUNZ ?????????.html',form=MessagesForm(),messages=messages)
     return render_template('DAPUNZ ?????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_20', methods=['GET','POST'])
def spot4_20():
     postid=73
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????.html',form=MessagesForm(),messages=messages)
     return render_template('?????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_21', methods=['GET','POST'])
def spot4_21():
     postid=74
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('Otto Pasta.html',form=MessagesForm(),messages=messages)
     return render_template('Otto Pasta.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_22', methods=['GET','POST'])
def spot4_22():
     postid=75
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('??????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_23', methods=['GET','POST'])
def spot4_23():
     postid=76
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_24', methods=['GET','POST'])
def spot4_24():
     postid=77
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_25', methods=['GET','POST'])
def spot4_25():
     postid=78
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('Kooks ????????? (K1 Danshui ????????????).html',form=MessagesForm(),messages=messages)
     return render_template('Kooks ????????? (K1 Danshui ????????????).html',form=MessagesForm(),messages=messages)

@app.route('/spot4_26', methods=['GET','POST'])
def spot4_26():
     postid=79
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????MeetEuropa.html',form=MessagesForm(),messages=messages)
     return render_template('????????????MeetEuropa.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_27', methods=['GET','POST'])
def spot4_27():
     postid=80
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????????????????-???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('?????????????????????-???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_28', methods=['GET','POST'])
def spot4_28():
     postid=81
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('Come See Pizza.html',form=MessagesForm(),messages=messages)
     return render_template('Come See Pizza.html',form=MessagesForm(),messages=messages)

@app.route('/spot4_29', methods=['GET','POST'])
def spot4_29():
     postid=82
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????? Henmi Kitchen.html',form=MessagesForm(),messages=messages)
     return render_template('???????????? Henmi Kitchen.html',form=MessagesForm(),messages=messages)

#????????????
@app.route('/spot5_1', methods=['GET','POST'])
def spot5_1():
     postid=83
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot5_2', methods=['GET','POST'])
def spot5_2():
     postid=84
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????.html',form=MessagesForm(),messages=messages)
     return render_template('?????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot5_3', methods=['GET','POST'])
def spot5_3():
     postid=85
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot5_4', methods=['GET','POST'])
def spot5_4():
     postid=86
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????? LiAng Le.html',form=MessagesForm(),messages=messages)
     return render_template('?????? LiAng Le.html',form=MessagesForm(),messages=messages)

@app.route('/spot5_5', methods=['GET','POST'])
def spot5_5():
     postid=87
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot5_6', methods=['GET','POST'])
def spot5_6():
     postid=88
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('??????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('??????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot5_7', methods=['GET','POST'])
def spot5_7():
     postid=89
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('???????????????.html',form=MessagesForm(),messages=messages)
     return render_template('???????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot5_8', methods=['GET','POST'])
def spot5_8():
     postid=90
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????????????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('?????????????????????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot5_9', methods=['GET','POST'])
def spot5_9():
     postid=91
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('?????????????????????.html',form=MessagesForm(),messages=messages)

@app.route('/spot5_10', methods=['GET','POST'])
def spot5_10():
     postid=92
     messages = Message.query.filter(Message.postid==postid).order_by(Message.timestamp.desc())
     form = MessagesForm()
     if request.method == 'POST':
          if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           message = Message(name=name, body=body,postid=postid)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return render_template('????????????????????????.html',form=MessagesForm(),messages=messages)
     return render_template('????????????????????????.html',form=MessagesForm(),messages=messages)


@app.route('/register',methods=['POST','GET'])
def register():
     form=RegisterForm()
     if form.validate_on_submit():
          comform_email=UserReister.query.filter_by(email=form.email.data).first()
          comform_id=UserReister.query.filter_by(userid=form.userid.data).first()
          email=UserReister.query.filter_by(email=form.email.data).first()
          if comform_email:
               flash('Email????????????')
               return render_template('register.html', form=form)
          if comform_id:
                flash('id????????????')    
                return render_template('register.html', form=form)
          anum=0
          lower_num=0
          upper_num=0   
          for i in form.password.data:
               if i.isdigit():
                    anum += 1
               elif i.islower():
                    lower_num += 1
               elif i.isupper():
                    upper_num += 1      
          if form.password.data !=form.password2.data:
                flash('???????????????')
                return render_template('register.html', form=form)
          if lower_num<=0 and upper_num<=0:
                flash('?????????????????????')
                return render_template('register.html', form=form) 
          if anum<=0:
               flash('?????????????????????')
               return render_template('register.html', form=form)            
          user = UserReister(userid = form.userid.data,email = form.email.data,password = form.password.data)
          db.session.add(user)
          db.session.commit()
          return redirect(url_for("login"))
     return render_template('register.html', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
     form = LoginForm()
     if form.validate_on_submit():
        user = UserReister.query.filter_by(email=form.email.data).first()
        password=UserReister.query.filter_by(password=form.password.data).first()
        if user:
            if password:
                session['userid']=request.values['userid']
                userid=session['userid']
                return render_template("index.html",userid=form.userid.data,values=Post.query.filter_by(author=userid),values1=Spot.query.order_by(func.rand()).limit(5))
            else:
                flash('Email???????????????')
        else:
            flash('???????????????Email??????')
     return render_template('login.html', form=form)


@app.route("/user")
def user():
    if "userid" in session:
        userid = session["userid"]
        return render_template("index.html",userid=userid,values=Post.query.filter_by(author=userid),values1=Spot.query.order_by(func.rand()).limit(5))
    else:
        return redirect(url_for("login"))


@app.route("/userpost")
def userpost():
    if "userid" in session:
        userid = session["userid"]
        return render_template("post.html",userid=userid,values=Post.query.filter_by(author=userid))
    else:
        return redirect(url_for("user"))

@app.route("/userrough")
def userrough():
     if "userid" in session:
        userid = session["userid"]
        return render_template("rough.html",userid=userid,values=Save.query.filter_by(author=userid))
     else:
        return redirect(url_for("user"))

@app.route('/<int:id>_edit', methods=['GET', 'POST'])
def edit(id):
    content = Save.query.filter_by(id=id).first()   
    userid = session["userid"]  
    form = PostForm(head=content.head,main=content.main, body=content.body,time=content.timestamp,tag=content.tag)
    if form.validate_on_submit():
     if form.upload.data == True:
          post = Post(head=form.head.data,main=form.main.data,body=form.body.data,timestamp=form.time.data,tag=form.tag.data,author=userid,like=0)
          post.head = form.head.data
          post.main=form.main.data
          post.body = form.body.data
          post.timestamp=form.time.data
          post.tag=form.tag.data
          post.author=userid
          Save.query.filter_by(id=id).delete()
          db.session.add(post)        
          db.session.commit()
          return redirect(url_for("user"))  
     elif form.save.data == True:
          save1=Save.query.get(id)
          save1.head = form.head.data
          save1.main=form.main.data
          save1.body = form.body.data
          save1.timestamp=form.time.data
          save1.tag=form.tag.data
          save1.author=userid
          db.session.commit()
          return render_template('rough.html')  
     else:
          return redirect(url_for("user"))    
    return render_template('adjust.html', form=form)     

@app.route("/userlike")
def userlike():
    if "userid" in session:
        userid = session["userid"]
        return render_template("like.html",userid=userid,values=Post.query.filter(collect.author==userid,Post.id==collect.postid).all())
    else:
        return redirect(url_for("user"))



@app.route("/useradjust", methods=['GET','POST'])
def useradjust():
     form=PostForm()
     userid = session["userid"]
     if form.validate_on_submit():
          if form.upload.data == True:
               post=Post(form.head.data,form.main.data,form.body.data,form.time.data,form.tag.data,userid,like=0)
               db.session.add(post)        
               db.session.commit()
               return redirect(url_for("user"))  
          elif form.save.data == True:
               save=Save(form.head.data,form.main.data,form.body.data,form.time.data,form.tag.data,userid)
               db.session.add(save)        
               db.session.commit()
               return redirect(url_for("user"))  
          else:
               return redirect(url_for("user"))             
     else:
          return render_template('adjust.html',form=form)    

@app.route('/spotlike_<int:post_id>_<userid>', methods=['post', 'get'])
def spotlike(post_id,userid):
     userid1 = session.get('userid')
     if(userid==userid1):
          flash('???????????????????????????')
          return render_template('??????????????????.html',values=Post.query.filter_by(tag='??????').all(),userid=userid1)
     elif(like.query.filter(like.author==userid1,like.postid==post_id).count()>0):
          flash('????????????')
          return render_template('??????????????????.html',values=Post.query.filter_by(tag='??????').all(),userid=userid1) 
     elif(userid1==None):
          flash('????????????')
          return render_template('login.html', form=LoginForm())
     else:
          likes=like(postid=post_id,author=userid1)
          a=Post.query.get(post_id)
          a.like=a.like+1
          db.session.add(likes)
          db.session.commit()
          return render_template('??????????????????.html',values=Post.query.filter_by(tag='??????').all(),userid=userid1)

@app.route('/foodlike_<int:post_id>_<userid>', methods=['post', 'get'])
def foodlike(post_id,userid):
     userid1 = session.get('userid')
     if(userid==userid1):
          flash('???????????????????????????')
          return render_template('??????????????????.html',values=Post.query.filter_by(tag='??????').all(),userid=userid1)
     elif(like.query.filter(like.author==userid1,like.postid==post_id).count()>0):
          flash('????????????')
          return render_template('??????????????????.html',values=Post.query.filter_by(tag='??????').all(),userid=userid1)
     elif(userid1==None):
          flash('????????????')
          return render_template('login.html', form=LoginForm())      
     else:
          likes=like(postid=post_id,author=userid1)
          a=Post.query.get(post_id)
          a.like=a.like+1
          db.session.add(likes)
          db.session.commit()
          return render_template('??????????????????.html',values=Post.query.filter_by(tag='??????').all(),userid=userid1)

@app.route('/spotcollect_<int:post_id>_<userid>', methods=['post', 'get'])
def spotcollect(post_id,userid):
     userid1 = session.get('userid')
     if(userid==userid1):
          flash('???????????????????????????')
          return render_template('??????????????????.html',values=Post.query.filter_by(tag='??????').all(),userid=userid1)
     elif(collect.query.filter(collect.author==userid1,collect.postid==post_id).count()>0):
          flash('????????????')
          return render_template('??????????????????.html',values=Post.query.filter_by(tag='??????').all(),userid=userid1)
     elif(userid1==None):
          flash('????????????')
          return render_template('login.html', form=LoginForm()) 
     else:
          a = collect(postid=post_id,author=userid1)
          db.session.add(a)
          db.session.commit()
          return render_template('like.html',values=Post.query.filter(collect.author==userid1,Post.id==collect.postid).all())

@app.route('/foodcollect_<int:post_id>_<userid>', methods=['post', 'get'])
def foodcollect(post_id,userid):
     userid1 = session.get('userid')
     if(userid==userid1):
          flash('???????????????????????????')
          return render_template('??????????????????.html',values=Post.query.filter_by(tag='??????').all(),userid=userid1)
     elif(collect.query.filter(collect.author==userid1,collect.postid==post_id).count()>0):
          flash('????????????')
          return render_template('??????????????????.html',values=Post.query.filter_by(tag='??????').all(),userid=userid1)
     elif(userid1==None):
          flash('????????????')
          return render_template('login.html', form=LoginForm())      
     else:
          a = collect(postid=post_id,author=userid1)
          db.session.add(a)
          db.session.commit()
          return render_template('like.html',values=Post.query.filter(collect.author==userid1,Post.id==collect.postid).all())

@app.route('/search', methods=['post', 'get'])
def search():
    content = request.form.get('content') 
    userid=session["userid"]
    if content is None:
        content = " "
    quotes = Post.query.filter(Post.head.like("%"+content) if content is not None else "").filter(Post.author==userid).all()
    return render_template('search.html',quotes = quotes,userid=userid) 

@app.route('/searchall', methods=['post', 'get'])
def searchall():
    content1 = request.form.get('content') 
    if content1 is None:
        content1 = " "
    values=Post.query.filter(Post.head.like("%"+content1) if content1 is not None else "").all()
    return render_template('searchall.html',values=values)

@app.route("/logout")
def logout():
    session.pop("userid", None)
    return redirect(url_for("index"))

@app.route("/submit", methods=['POST','GET'])
def submit():
     form = SuggestForm()
     if request.method == 'POST':
         if form.validate_on_submit():
           name = form.name.data
           body = form.body.data
           email=form.email.data
           message = Suggest(name=name, body=body,email=email)
           db.session.add(message)
           db.session.commit()
           flash('????????????')  
           return redirect(url_for("index"))

if __name__ == "__main__":
     app.run('0.0.0.0')