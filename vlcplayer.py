import vlc
import time
import playlistCreate

import schedule
import re


# creating a media player object
media_player = vlc.MediaListPlayer()

# creating Instance class object
player = vlc.Instance()

# creating a new media list object
media_list = player.media_list_new()

index = 0
for x in playlistCreate.playlist:
    eplink = playlistCreate.playlist[index]['url']
    media = player.media_new(eplink)
    # adding media to media list
    media_list.add_media(media)
    index += 1

# setting media list to the media player
media_player.set_media_list(media_list)

# start playing video
media_player.play()
 


def obsText(playlist):

    podcastSource = media_player.get_media_player().get_media().get_mrl()


    for item in playlist:
        if item['url'] == podcastSource:
            nowPlaying = item['showTitle']
            nowPlaying2 = item['title']
            nowPlayingPD = item['pubDate']

    #format pubdate        
    #nowPlayingPDSplit = nowPlayingPD.split(r" ^[0-9][0-9]:", 1)
    
    #nowPlayingPD = nowPlayingPDSplit[0]
    with open('nowplaying.txt', 'w', encoding='utf-8') as txt:
        txt.write('Now Playing: ' + nowPlaying)
    with open('nowplaying2.txt', 'w', encoding='utf-8') as txt:
        txt.write(nowPlaying2)
    with open('nowplayingPD.txt', 'w', encoding='utf-8') as txt:
        txt.write(nowPlayingPD)
    print("Now Playing: ", nowPlaying, " - ", nowPlaying2)
    print("Published: ", nowPlayingPD)

# Scheduling functions ()   

schedule.every(30).seconds.do(obsText, playlistCreate.playlist)

while True:
    schedule.run_pending()
    time.sleep(1)

#   play next video (cmd line)
#   media_player.next()
#   media_player.audio_get_track()
#   every 5 minutes check if audio changed 
    #by running source()
#       audioFileName = 
#       media_player.get_media_player().get_media().get_mrl()
#           if PARTOFURL in PATH: 
#               TITLE = BIGSHINYTAKES
#               WRITE A TXT FILE TO SAY - WHAT IS THE 
#           ELIF PARTOFURL IN PATH
#               TITLE = 