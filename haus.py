'''
TRANSISTOR FEED SCRAPER

'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://feeds.transistor.fm/haus-of-decline'

headers = {
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
}

html = urlopen(url)
soup = BeautifulSoup(html.read(), 'html.parser')


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

successMsg = '- Haus of Decline episode list built'