from urllib.request import urlopen
from bs4 import BeautifulSoup


import vlc
import time


#####
 
# creating a media player object
media_player = vlc.MediaListPlayer()
  
# creating Instance class object
player = vlc.Instance()
  
# creating a new media list object
media_list = player.media_list_new()

#####

urlArray = ['https://feeds.buzzsprout.com/972934.rss', 'https://feeds.transistor.fm/haus-of-decline']

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
    # creating a new media
    # put this in a for loop and randomize the number to play all the episodes urls stored in a list
    # randomly add from df to medialist then remove it from df 

    media = player.media_new(epUrl)
    
    # adding media to media list
    media_list.add_media(media)


epLink = df[0]['url']



  

  
# setting media list to the media player
media_player.set_media_list(media_list)
  
  
# start playing video
media_player.play()

#limit to 30 mins
#play next video (cmd line)
#media_player.next()

def playlist(df):
    for x in df:
        print(df[x]['title'])
