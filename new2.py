from bs4 import BeautifulSoup
import requests

try:
    url= "https://play.google.com/store/apps/collection/cluster?clp=igM4ChkKEzUyNTg0MTA1Mzg1MzAzMzE1MDgQCBgDEhkKEzUyNTg0MTA1Mzg1MzAzMzE1MDgQCBgDGAA%3D:S:ANO1ljKvxO0&gsr=CjuKAzgKGQoTNTI1ODQxMDUzODUzMDMzMTUwOBAIGAMSGQoTNTI1ODQxMDUzODUzMDMzMTUwOBAIGAMYAA%3D%3D:S:ANO1ljIaI2Q"
    page= requests.get(url)
    soup= BeautifulSoup(page.content, 'html.parser')
    app = soup.findAll('a', class_ = 'title', limit=None)
    print(len(app))
    print("----------APPS BY THIS DEVELOPER-------------")
    i=0
    while i< len(app):
        print(app[i].text)
        i=i+1
		
except Exception as e:
    print(e)


