from flask_sqlalchemy import SQLAlchemy
from app import db
from scrapped import finl_all

class Course(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    course_name = db.Column(db.string(100))
    course_link = db.Column(db.string(100))
    course_priceInr = db.Column(db.float)
    course_priceUsd = db.Column(db.float)
    courseLanguage =db.Column(db.string(100))
    course_mode = db.Column(db.string(100))
    course_keyword = db.Column(db.string(100))
    