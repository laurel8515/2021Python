# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 12:24:08 2021

@author: user
"""

import requests
from bs4 import BeautifulSoup
import os

#寫成副程式
def get_pic(url,c):
    resp=requests.get(url)
    with open(imgdir+'icon'+str(c)+'.png','wb')as fobj:
        fobj.write(resp.content)
        
imgdir='flaticon/'
if not os.path.exists(imgdir):
    os.mkdir(imgdir)

url='https://www.flaticon.com/packs/birds-34'
resp=requests.get(url)
if resp.status_code==200:
    with open('flaticon_birds.html','w',encoding='utf-8')as fobj:
        fobj.write(resp.text)
        #print(resp.text)

    soup=BeautifulSoup(resp.text,'html.parser')
    ultag=soup.find('ul','icons')
    
    #imglist=ultag.find_all('img')
    iconitem=ultag.find_all('li','icon--item')


    count=0
    for i in iconitem:
        try:
            print(i['data-png'])
            get_pic(i['data-png'],count)
        except:
            continue
        count+=1
        print('**********************')