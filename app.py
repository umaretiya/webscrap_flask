from flask import Flask,request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from bs4 import BeautifulSoup as bs
import json
from logger import Logger
from scrapped import catgory_Courses,categories_distributins,finl_all
from course_page import course_page, mentor
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///course.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


log = Logger.logger_func()

@app.route('/')
def home():
    mainCat = categories_distributins()[0:10]
    subCat = categories_distributins()[10:]    
    log.info("Home functions creating main and sub category")
    return  render_template('index.html',mainCategory=mainCat, courses=finl_all()[0:])

@app.route("/bifurcat", methods = ['GET','POST'])
def catgory_bifurcat():
    if request.method == 'POST':
        name = request.form['bifurcat']
        log.info("category bifurcation of category course")   
        return render_template('bifurcat.html', category =catgory_Courses())
    
@app.route("/category", methods = ['GET','POST'])
def catgory_check():
    if request.method == 'POST':
        name = request.form['catGory']
        mainCat = categories_distributins()[0:10]
        subCat = categories_distributins()[10:]   
        log.info("Category check functions")
        return render_template('category_course.html', categories =catgory_Courses()[0:])
    

@app.route('/courseLink', methods=['GET','POST'])
def individualCouseDetails():
    if request.method == 'POST':
        name = request.form['link']
        # https://courses.ineuron.ai/MERN-Stack-Bootcamp
        course_name = name.split('/')[-1]
        log.info("single course details ,fatching a data of single course")
        return render_template('individual_courseData.html',courselink=course_page(name),course_name=course_name, mentor_name=mentor(name))


@app.route('/scrapp', methods = ['GET','POST'])
def webScrapp():
    if request.method == 'POST':
        url = request.form['submit']
        req  = requests.get(url)
        main_page = bs(req.content,'html.parser')
        raw_json = main_page.find('script')
        #main_json= json.loads(raw_json)
        ulr_new = url
        name = {'url':ulr_new}      
        log.info("Scrappped full web scrapping data: Webscrapp functon")
        return render_template('results.html',courses_data=finl_all()[0:])



if __name__ == '__main__':
    log.info("App is run: main")
    app.run()