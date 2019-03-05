from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import timedelta, date
from nltk.corpus import stopwords 
import nltk as nl
import requests, zipfile, io
import pandas as pd
import numpy as np
import glob
import tensorflow as tf
import tflearn

def daterange(start_date, end_date):
    if int((end_date - start_date).days) >= 0:
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)
    else:
        for n in range(-1,int((end_date - start_date).days),-1):
            n_date = start_date + timedelta(n)
            if n_date.weekday() < 5:
                yield start_date + timedelta(n)

def prevworkingday(today_date):
    d_date = date(2006, 1, 1)
    for i in daterange(today_date,d_date):
        return i

## Getting unique SC_CODE from all files
df = pd.concat([pd.read_csv(f) for f in glob.glob('C:\\Drives\\Zunk\\try\\tick\\*.csv')])
all_sccode = set(df.SC_CODE)
print(len(all_sccode))

## Creating unique words from all news files
df = pd.concat([pd.read_csv(f,sep='\n', header=None) for f in glob.glob('C:\\Drives\\Zunk\\try\\newz\\*.txt')])
df['tokens'] = [nl.word_tokenize(s[0]) for _,s in df.iterrows()]
words = []
for i in df.tokens:
    words.extend(i)

words = [word for word in words if len(word) > 2] 
stop_words = set(stopwords.words('english')) 
words = [w.lower() for w in words if not w.lower() in stop_words]
words.sort()

print("================================== Stemming ==================================",len(words))
lemma = nl.wordnet.WordNetLemmatizer()
words = [lemma.lemmatize(word) for word in words]
stemmer = nl.stem.PorterStemmer()
words = [stemmer.stem(word) for word in words]
words = set(words)
print("================================== Unique words ==================================",len(words))


### DATA PREP 
start_date = date(2019, 1, 2)
end_date = date(2019, 2, 1)

X,Y = [],[]

for i,single_date in enumerate(daterange(start_date, end_date)):
    if single_date.weekday() < 5:
      
        #============= ET PART ===========================================
        # open file b4 day file
        # make matrix out of all words
        prev_date = prevworkingday(single_date)
        ddmmyy = prev_date.strftime("%d%m%y")
        f1 = 'C:\\Drives\\Zunk\\try\\newz\\NW'+ddmmyy+'.txt'
        n_df = pd.read_csv(f1, sep='\n', header=None)
        n_df['tokens'] = [nl.word_tokenize(s[0]) for _,s in n_df.iterrows()]
        file_words = []
        for t in n_df.tokens:
            file_words.extend(t)
        file_words = [word for word in file_words if len(word) > 2]  
        file_words = [w.lower() for w in file_words if not w.lower() in stop_words]
        file_words = [lemma.lemmatize(word) for word in file_words]
        file_words = [stemmer.stem(word) for word in file_words]
        onehot = []
        for word in words:
            onehot.append(1) if word in file_words else onehot.append(0)
        X.append(onehot)
        print(sum(X[i]),len(X[i]))
        
        #============= NW PART ===========================================
        # open today file
        # make matrix of top 10 scrip codes out of all scrip codes
        ddmmyy = single_date.strftime("%d%m%y")
        f2 = 'C:\\Drives\\Zunk\\try\\tick\\EQ'+ddmmyy+'.csv'
        t_df = pd.read_csv(f2)
        t_df['CHG'] = 100*(t_df.CLOSE - t_df.PREVCLOSE)/t_df.PREVCLOSE
        td = t_df[['SC_CODE','SC_NAME','CHG']][(t_df != 0).all(1)].sort_values(['CHG'],ascending=False).head(10).SC_CODE
        onehot = []
        for code in all_sccode:
            onehot.append(1) if code in td.values else onehot.append(0)
        Y.append(onehot)
        print(sum(Y[i]), len(Y[i]))
        break
        print("==============================================")