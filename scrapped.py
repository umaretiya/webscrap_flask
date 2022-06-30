from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import requests
import json

url = "https://courses.ineuron.ai/"
s = HTMLSession()
r =  s.get(url)    
full_site = bs(r.content,'html.parser')
full_siteData = full_site.find_all('script',{'id':'__NEXT_DATA__'})
main_site = json.loads(full_siteData[0].string)

main_json =main_site['props']['pageProps']['initialState']['init']['courses']
courses_name = [i for i in main_json.keys()]
instructors = main_site['props']['pageProps']['initialState']['init']['instructors']
instrucotr_names =[instructors[i]['name'] for i in instructors]
category = main_site['props']['pageProps']['initialState']['init']['categories']

    
def categories_distributins():
    finalList = []
    mainCate = {}
    mainList = []
    mainC = []
    subC = []
    subList = []
    category = main_site['props']['pageProps']['initialState']['init']['categories']
    for i,j in category.items():
        main_name = category[i]['title']      
        mainCate = {'mainCatogory':main_name} 
        mainList.append(mainCate)
        for k in j['subCategories']:
            sub_name= j['subCategories'][k]['title']
            subCat = {'subCategory':sub_name}
            subList.append(subCat)
            
    finalList.extend(mainList)# + subList)
    finalList.extend(subList)
    return finalList


def catgory_Courses():
    allcat_list = []
    cateDict= {}
    category = main_site['props']['pageProps']['initialState']['init']['categories']
    for i in category:    
        #cateDict= {'mainCategory':category[i]['title']}
        cateDict= {'mainCategory':category[i]['title'],'SubCategory':[category[i]['subCategories'][j]['title'] for j in category[i]['subCategories'] ]}
        allcat_list.append(cateDict)
    return allcat_list
        


def finl_all():
    full_summry = []

    url = "https://courses.ineuron.ai/"
    s = HTMLSession()
    r =  s.get(url)
    full_site = bs(r.content,'html.parser')
    full_siteData = full_site.find_all('script',{'id':'__NEXT_DATA__'},type="application/json")
    main_site = json.loads(full_siteData[0].string)
    main_json =main_site['props']['pageProps']['initialState']['init']['courses']
    
    for i,j in main_json.items():
        try:
            if j['pricing']['isFree'] != True:
                course_name = i
                course_link = url + i.replace(" ","-")
                course_priceInr = j['pricing']['IN'] 
                course_priceUsd = j['pricing']['US']
                courseLanguage = j['courseMeta'][0]['overview']['language']
                course_mode = j['mode']
                course_keyword =j['seo']['keywords'] 
                full_dataDict = {'Course-Name':course_name,
                                 'Course-Link':course_link,
                                 'Price-INR':course_priceInr,
                                 'Price-USD':course_priceUsd,
                                 'Course-Language':courseLanguage,
                                 'Course_Mode':course_mode,
                                 'KeyWords':course_keyword,
                                }
                full_summry.append(full_dataDict)
            else:
                course_name = i
                course_free = j['pricing']['isFree']
                courseLanguage = j['courseMeta'][0]['overview']['language']
                course_mode = j['mode']
                course_keyword =j['seo']['keywords'] 
                full_dataDict = {'Course-Name':course_name,                            
                                 'Course-Link':course_link,
                                 'course_Fee':0.0,

                                 'Course-Language':courseLanguage,
                                 'Course_Mode':course_mode,
                                 'KeyWords':course_keyword,
                                }
                full_summry.append(full_dataDict)

        except:
            course_name = i  
            course_priceInr = j['batches'][0]['pricing']['IN']
            course_priceUsd = j['batches'][0]['pricing']['US']
            courseLanguage = j['courseMeta'][0]['overview']['language']
            course_mode = j['mode']
            course_keyword =j['seo']['keywords'] 
            full_dataDict = {'Course-Name':course_name,
                             'Course-Link':course_link,
                             'Price-INR':course_priceInr,
                             'Price-USD':course_priceUsd,
                             'Course-Language':courseLanguage,
                             'Course_Mode':course_mode,
                             'KeyWords':course_keyword,
                            }
            full_summry.append(full_dataDict)
    return full_summry
    

#print(len(catgory_Courses()))
#print(len(categories_distributins()))
#print(catgory_Courses())