from difflib import SequenceMatcher
import requests
import json
import traceback
import play_scraper
from bs4 import BeautifulSoup
from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy

dict = {}
name = []
pckn = []
c = {}
c_no = 1


def details(pkname):
    try:
        dev = play_scraper.details(pkname)
        # print(dev)
        for key in dev:
            if key == 'developer_id':
                # print(key+ " "+ dev[key])
                devid = dev[key]
                return devid
    except Exception as e:
        print(e)


def get_apps(dv):
    try:
        url = "https://play.google.com/store/apps/dev?id=" + dv
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        apps = soup.find('div', class_="g4kCYe")
        ap = apps.findAll('a')
        p = str(ap[0])
        q = p.split('href="')
        r = str(q[1])
        s = r.split('" jslog')
        t = s[0]
        # print(t)
        return t

    except Exception as e:
        print(e)


def apps_by_dev(clp):
    try:
        pages = requests.get(clp)
        soups = BeautifulSoup(pages.content, 'html.parser')
        app = soups.findAll('a', class_='title')
        xyz = soups.findAll('div', class_='card-content id-track-click id-track-impression')
        j = 0
        while j < len(xyz):
            a = str(xyz[j]).split('data-docid="')
            b = a[1].split('" data-server-cookie')
            pck = b[0]
            pckn.append(pck)
            # print(pckn)
            # print(xyz[j])
            j = j + 1
        # print(xyz)
        print('----------OTHER APPS BY THIS DEVELOPER----------')
        i = 0
        while i < len(app):
            name.append(app[i].text)
            print(app[i].text)
            i = i + 1
        return app

    except Exception as e:
        print(e)	

def compare(a,b):
    try: 
        return SequenceMatcher(None, a, b).ratio()
	   
    except Exception as e:
        print(e)

def sim(AppName, AppPackage, row, c_no):
    print("----SIMILAR APPS----")
    c_no = 1
    for keys in dict:
        com = compare(keys.strip(), AppName.strip())
        com = com * 100
        comp = compare(dict[keys].strip(), AppPackage.strip())
        comp = comp * 100
        #print(com)
        if com >= 65 and comp >= 65:
            print(keys + " " + dict[keys]+ " " + str(com)+ " "+ str(comp))
            to_excel(keys, dict[keys], row, c_no)
            c_no = c_no + 1
        else:
            pass
    dict.clear()
    return c_no


def to_excel(appName, appPackage, row_, c_no):
    rb = open_workbook("app_det.xls", 'w')
    wb = copy(rb)
    s = wb.get_sheet(0)
    c[appName] = appPackage
    print(c)
    for keys in c:
        s.write(row_, c_no, c[keys])
    print('written')
    wb.save("app_det.xls")


# pn=input("enter package name for app: ")
loc = "app_det.xls"
wb = open_workbook(loc)
sheet = wb.sheet_by_index(0)
col = 0
rows = 1
while rows < sheet.nrows:
    pn = sheet.cell_value(rows, col)
    print(pn)
    DEVID = details(pn)
    moreApps = get_apps(DEVID)
    apps_by_dev(moreApps)
    devel = play_scraper.details(pn)
    i = 0
    while i < len(name):
        dict[name[i]] = pckn[i]
        i = i + 1
    for val in devel:
        if val == "title":
            Title = devel[val]
            c_no = sim(Title, pn, rows, c_no)
    #print(dict)
    rows = rows + 1
# appName= details(pn)
# appPackage= get_apps(x)
# fin(appPacakge)
# print(x)
# devel= play_scraper.details(pn)
# for val in devel:
# if val=="title":
# Title=devel[val]
# print(Title)
# i=0
# while i<len(name):
# dict[name[i]]=pckn[i]
# i=i+1
# print(opp)
# sim(pn,rt)
