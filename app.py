import re
import requests
import json
import traceback
import play_scraper
from bs4 import BeautifulSoup

def details(pkname):
    try:
        dev= play_scraper.details(pkname)
        for key in dev:
            if key=='developer':
                print(key+ " "+ dev[key])
            if key=='developer_id':
                print(key+ " "+ dev[key])
                devid= dev[key]
                return devid
    except Exception as e:
        print(e)

def get_apps(dv):
    try:
        url= "https://play.google.com/store/apps/dev?id="+ dv
        page= requests.get(url)
        soup= BeautifulSoup(page.content, 'html.parser')
        apps= soup.find('div',class_ ="g4kCYe")
        ap= apps.findAll('a')
        p= str(ap[0])
        q= p.split('href="')
        r= str(q[1])
        s= r.split('" jslog')
        t= s[0]
        #print(t)
        return t
	
    except Exception as e:
	    print(e)

def fin(clp):
    try:
        pages= requests.get(clp)
        soups= BeautifulSoup(pages.content, 'html.parser')
        app = soups.findAll('a', class_ = 'title')
        print('----------OTHER APPS BY THIS DEVELOPER----------')
        i=0
        while i< len(app):
            print(app[i].text)
            i=i+1
		
    except Exception as e:
        print(e)

pn=input("enter package name for app: ")		
x= details(pn)
y= get_apps(x)
fin(y)
	