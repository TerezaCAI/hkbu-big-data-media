import requests
from bs4 import BeautifulSoup
import csv
import re 

hacker='https://news.ycombinator.com/'

title=[]
score=[]
# web=[]
time=[]
for i in range(1,100):
	url=hacker+'news?p='+str(i)
	r=requests.get(url).text
	page=BeautifulSoup(r,'html.parser')
	area=page.find_all('a',attrs={'class':'storylink'})
	for t in area:
		title.append(t.text)
	subtext=page.find_all('span',attrs={'class':'score'})
	for s in subtext:
		score.append(s.text)
	age=page.find_all('span',attrs={'class':'age'})
	for a in age:
		time.append(a.text)
with open('hw2.csv','w') as f:
	writer=csv.writer(f)
	header=['title','score','time']
	writer.writerow(header)
	rows=zip(title,score,time)
	for row in rows:
		writer.writerow(row)

