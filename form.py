import email
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,TextAreaField,DateField,EmailField,PasswordField,BooleanField
from wtforms.validators import DataRequired,EqualTo


class RegisterForm(FlaskForm):
    userid = StringField(u'帳號', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField(u'密碼', validators=[DataRequired()])
    password2 = PasswordField(u'確認密碼', validators=[DataRequired()])
    submit = SubmitField(u'註冊')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    userid = StringField(u'帳號', validators=[DataRequired()])
    password = PasswordField(u'密碼', validators=[DataRequired()])
    remember_me = BooleanField(u'保持登入')
    submit = SubmitField(u'登入')

class PostForm(FlaskForm):
    head=StringField(u"名稱", validators=[DataRequired()])
    main=StringField(u"主旨", validators=[DataRequired()])
    time=DateField(u"日期",validators=[DataRequired()])
    body =TextAreaField(u"景點介紹", validators=[DataRequired()])
    tag=SelectField(u"類別", choices=[ ('類別', '選擇類別'),('景點', '景點'), ('美食', '美食')])
    back= SubmitField(u'返回')
    save=SubmitField(u'儲存貼文')
    upload = SubmitField(u'確認發布')

class AdjustForm(FlaskForm):
    adjust=SubmitField(u'修改')
    upload = SubmitField(u'發布')

class LikeForm(FlaskForm):
   like=SubmitField(u'收藏')

class MessagesForm(FlaskForm):
    name = StringField(u'會員帳號', validators=[DataRequired()])
    body = StringField(u'留言', validators=[DataRequired()])
    submit = SubmitField(u'留言')

class SuggestForm(FlaskForm):
    name = StringField(u'姓名', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    body = StringField(u'留言/想法', validators=[DataRequired()])
    submit = SubmitField(u'留言')    