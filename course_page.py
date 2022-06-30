from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import requests
import json

def course_page(course_link):
    course_link_s = HTMLSession()    
    #course_link = requests.get("https://courses.ineuron.ai/"+ course_full_name.replace(" ","-").title())
    #print(r.status_code)
    course_link = requests.get(course_link)
    course_soup = bs(course_link.content,'html.parser')
    course_siteData = course_soup.find('script',src=None)
    course_json = json.loads(course_siteData.string)
    try:
        isJobGuaranteeProgram = course_json['props']['pageProps']['data']['isJobGuaranteeProgram']
    except:
        isJobGuaranteeProgram = "NA"
    requirements = course_json['props']['pageProps']['data']['meta']['overview']['requirements']
    course_feature =course_json['props']['pageProps']['data']['meta']['overview']['features']
    description = course_json['props']['pageProps']['data']['details']['description']    
    def curriculum_data():
        curriculumList = []
        curriculum =course_json['props']['pageProps']['data']['meta']['curriculum']
        for i in curriculum:
            heading = curriculum[i]['title']
            curriculum_data = {'heading':heading, "description":[j['title'] for j in curriculum[i]['items']]}            
            curriculumList.append(curriculum_data)
        return curriculumList
    course_page = {'JobGuaranteeProgram':isJobGuaranteeProgram,
                  'Requirements': requirements,
                  'course_feature':course_feature,
                  'Description':description,
                  'Curriculum':curriculum_data(),
                  }
    return course_page

def mentor(course_link):
    instructor_data= []
    course_link_s = HTMLSession()    
    #course_link = requests.get("https://courses.ineuron.ai/"+ course_full_name.replace(" ","-").title())
    #print(r.status_code)
    course_link = requests.get(course_link)
    course_soup = bs(course_link.content,'html.parser')
    course_siteData = course_soup.find('script',src=None)
    course_json = json.loads(course_siteData.string)
    instructors =  course_json['props']['pageProps']['initialState']['init']['instructors']
    for i in instructors:
        instructor_name = instructors[i]['name']
        try:            
            instructor_email = instructors[i]['email']
        except:
            instructor_email = "Email Not available"
        try:            
            instructor_desc = instructors[i]['description']
        except:
            instructor_desc = 'Description not available'
        ins_data = {'instructor_name':instructor_name,
                    'instructor_email':instructor_email,
                    'instructor_desc':instructor_desc,
                    }
        instructor_data.append(ins_data)
    return instructor_data

#print(course_page('https://courses.ineuron.ai/MERN-Stack-Bootcamp'))
