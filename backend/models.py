from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from time import time
from flask_security import UserMixin, RoleMixin
from sqlalchemy.types import JSON

#Initialize db Object
db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String,unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    pref_subjects = db.Column(JSON)
    
    fs_uniquifier = db.Column(db.String, unique = True, nullable = False)
    active = db.Column(db.Boolean, default = True)
    roles = db.relationship('Role', backref = 'bearers', secondary = 'user_roles')
    scores = db.relationship('Scores', backref='user', lazy='dynamic' ,cascade="all, delete-orphan")
    
    
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)    



class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    
    
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False, unique = True)
    description = db.Column(db.String,nullable = False)
    chapters = db.relationship('Chapter', backref='subject', lazy='dynamic', cascade="all, delete-orphan")
    
    
class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    quizes = db.relationship('Quiz', backref='chapter',
                             lazy='dynamic', cascade="all, delete-orphan")
    
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'))
    date = db.Column(db.DateTime, index = True, default = datetime.now())
    duration = db.Column(db.Time, nullable = False)
    remarks = db.Column(db.String)
    questions = db.relationship(
        'Questions', backref='quiz', lazy='dynamic', cascade="all, delete-orphan")
    scores = db.relationship('Scores', backref='quiz',
                             lazy='dynamic', cascade="all, delete-orphan")

    
    
class Questions(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    statement = db.Column(db.String, nullable = False)
    option_1 = db.Column(db.String, nullable = False)
    option_2 = db.Column(db.String, nullable = False) 
    option_3 = db.Column(db.String, nullable = False)
    option_4 = db.Column(db.String, nullable = False)
    correct_answer = db.Column(db.String, nullable = False)
    marks = db.Column(db.Float, nullable = False)
    
class Scores(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    time = db.Column(db.DateTime, index = True, default = datetime.now())
    total_score = db.Column(db.Integer, nullable = True)
    attempts = db.Column(db.Integer, nullable = False)
    
class QuizAttendance(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable = False)
    visit_time = db.Column(db.DateTime, index=True, default=datetime.now())
    
    __table_args__ = (db.UniqueConstraint('user_id','quiz_id',name='_user_quiz_uc'),)
    
    
    
    
        
     
    
    