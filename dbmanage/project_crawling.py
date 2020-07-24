import requests
import xmltodict
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd

#regnum_list=[]
#noticeend_list=[]
#age_list=[]
#color_list=[]
#animal_list=[]
#species_list=[]
#neuteryn_list=[]
#sex_list=[]
#feature_list=[]
#weight_list=[]
#status_list=[]


import sqlite3
conn=sqlite3.connect('./test_web/db.sqlite3')
query='CREATE TABLE animalinfo (regnum INT, noticeend INT, age REAL, color TEXT, animal REAL, species TEXT, neuteryn TEXT, sex TEXT, feature REAL, weight REAL, status TEXT)'
conn.execute(query)
conn.commit()
conn.close

for i in range(1, 130):
    url="http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey=Ymw9TAM%2F6p5qafOIRjCH2%2BPgeLNyNm4mwzowKDYJ9imPeOO%2FpJW6aGma%2BZs3W8tguq7gXODSBOq9dXiRscn0Tw%3D%3D&bgnde=20140601&endde=20200630&upkind=&kind=&upr_cd=&org_cd=&care_reg_no=&state=&pageNo="+str(i)+"&numOfRows=5000&neuter_yn=&"
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

        with sqlite3.connect('./test_web/db.sqlite3') as con:
            cur=con.cursor()
            cur.execute("INSERT INTO animalinfo(regnum,noticeend,age,color,animal,species,neuteryn,sex,feature, weight, status) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (regnum, noticeend, age, color, animal, species, neuteryn, sex, feature, weight, status))
            con.commit()
        print('task_completed')
