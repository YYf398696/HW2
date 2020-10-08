#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import pandas as pd
from bs4 import BeautifulSoup


def extract_company(text):
    return text.split('Name:')[-1]
def extract_purpose(text):
    return text.split('Purpose:')[-1]
df=pd.DataFrame(columns=['CompanyName','Purpose'])


URL = 'http://3.95.249.159:8000/random_company'



company=[]
purpose=[]
for i in range(50):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    li_elem = soup.find_all('li')
    for li in li_elem:
        if li.text.find('Purpose:')==0:
            purpose.append(extract_purpose(li.text))
        elif li.text.find('Name:')==0:
            company.append(extract_company(li.text))
        else:
            continue
df['CompanyName']=company
df['Purpose']=purpose
df.to_csv('company.csv')



