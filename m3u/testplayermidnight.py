import vlc
import time 

media = vlc.MediaPlayer("test2.m3u")
media.play()

while True:
    print("still True")
    time.sleep(1)