# DATA PREP

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import timedelta, date
import requests, zipfile, io
import pandas as pd
import numpy as np


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

et_counter = 43466    #Start counter for 1st Jan    
start_date = date(2019, 1, 1)
end_date = date(2019, 2, 1)

for single_date in daterange(start_date, end_date):
    if single_date.weekday() < 5:
        yyyy= single_date.strftime("%Y")
        m = str(int(single_date.strftime("%m")))
        et_url = 'https://economictimes.indiatimes.com/archivelist/year-' + yyyy +',month-' + m + ',starttime-' + str(et_counter) +'.cms'
      
        #============= ET PART ===========================================
        req = Request(et_url, headers={'User-Agent': 'Mozilla/5.0'})
        pg = urlopen(req).read()
        soup = BeautifulSoup(pg)
        a_links = soup.find('section', attrs={'id': 'pageContent'}).find_all('a')
        eachday = ""
        for i,a in enumerate(a_links):
            if i > 2:
                eachday += a.text
        with open("C:\\Drives\\Zunk\\try\\newz\\NW" + single_date.strftime("%d%m%y") + ".txt", "w", encoding='utf-8') as text_file:
            text_file.write(eachday)
        print(et_counter)
    et_counter = et_counter + 1