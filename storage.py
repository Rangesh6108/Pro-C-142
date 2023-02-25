import csv

all_articles=[]

with open('articles.csv','r',encoding='utf-8') as f:
    dataframe=csv.reader(f)
    df=list(dataframe)
    all_articles=df[1:]

liked_articles=[]
not_liked_articles=[]