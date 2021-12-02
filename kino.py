'''
BUZZSPROUT FEED SCRAPER

'''
import urllib.request
from bs4 import BeautifulSoup

import pandas as pd

url = 'https://feeds.buzzsprout.com/226175.rss'

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'


headers = {
    'User-Agent':user_agent,
}

request = urllib.request.Request(url,None,headers) 
response = urllib.request.urlopen(request)
data = response.read() 
soup = BeautifulSoup(data, features="lxml")                #make BeautifulSoup
prettyHTML = soup.prettify()   #prettify the html

showTitle = soup.find('title').text
showDesc = soup.find('description').text
showImage = soup.find('url').text

items = soup.find_all('item')

df = []

limit = 0
for item in items: 

    limit += 1
    if limit > 5:
        break

    title = item.find('title').text
    pubDate = item.find('pubdate').text
    desc = item.find('description').text
    audioData = item.find('enclosure')
    epUrl = audioData['url']
    epTime = audioData['length']
    epObj = {'showTitle':showTitle, 'showDesc':showDesc,'showImg':showImage, 'title': title, 'pubDate': pubDate, 'description' : desc, 'url' : epUrl, 'audioDuration': epTime }
    epObj_copy = epObj.copy()
    df.append(epObj_copy)
    


successMsg ='----- Kino Lefter episode list built'