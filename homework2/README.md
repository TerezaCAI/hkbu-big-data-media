# Hacker News dataset

## This dataset contains the latest news scraped from the website.
startingpage:'https://news.ycombinator.com/'

## Data fields

* 'title'-string eg:A Career Cold Start Algorithm
* 'score'-string eg:95 points
* 'times'-string eg:1 hour ago

## code:
* Line15-17:
for every item in the tag ''a',attrs={'class':'storylink'}', get its text and add into the list called 'title'.
* Line18-20
for every item in the tag ''span',attrs={'class':'score'}', get its text and add into the list called 'score'.
* Line21-23 is same as above.
