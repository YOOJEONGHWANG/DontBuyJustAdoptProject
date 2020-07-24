
from background_task import background
import time
import requests
from bs4 import BeautifulSoup
import sqlite3
#from django.contrib.auth.models import User
import requests
import xmltodict
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd



@background()
def task_crawling_notice(schedule=60*60, repeat=59*59*24):
    conn=sqlite3.connect('db.sqlite3')
    conn.commit()
    conn.close

for i in range(1, 2):
    url="http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey=Ymw9TAM%2F6p5qafOIRjCH2%2BPgeLNyNm4mwzowKDYJ9imPeOO%2FpJW6aGma%2BZs3W8tguq7gXODSBOq9dXiRscn0Tw%3D%3D&bgnde=20200701&endde=20200731&upkind=&kind=&upr_cd=&org_cd=&care_reg_no=&state=&pageNo="+str(i)+"&numOfRows=5000&neuter_yn=&"
    resultxml=urlopen(url)
    result=resultxml.read()
    xmlsoup=BeautifulSoup(result, 'lxml-xml')
    items=xmlsoup.findAll("item")
    for item in items:
        regnum=item.find('desertionNo').text
        #regnum_list.append(regnum)
        noticeend=item.find('noticeEdt').text
        #noticeend_list.append(noticeend)
        age=item.find('age').text
        #age_list.append(age)
        color=item.find('colorCd').text
        #color_list.append(color)
        kind=item.find('kindCd').text
        if '개' in kind:
            animal='개'
        elif '고양이' in kind:
            animal='고양이'
        else:
            animal=None 
        species=kind.split(" ", maxsplit=2)[1]
        #animal_list.append(animal)
        #species_list.append(species)
        neuteryn=item.find('neuterYn').text
        #neuteryn_list.append(neuteryn)
        sex=item.find('sexCd').text
        #sex_list.append(sex)
        feature=item.find('specialMark').text
        #feature_list.append(feature)
        weight=item.find('weight').text
        #weight_list.append(weight)
        status=item.find('processState').text
        #status_list.append(status)

        with sqlite3.connect('db.sqlite3') as con:
            cur=con.cursor()
            cur.execute("INSERT INTO animalinfo(regnum,noticeend,age,color,animal,species,neuteryn,sex,feature, weight, status) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (regnum, noticeend, age, color, animal, species, neuteryn, sex, feature, weight, status))
            con.commit()
        
        time_tuple=time.localtime()
        time_str=time.strftime("%m%d%Y, %H:%M:%S", time_tuple)
    
        print('task_completed', regnum, animal, time_str)
