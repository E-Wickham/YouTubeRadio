import haus
import bigshiny
import inews
import dcj
import kino
import harbinger
import badandb
import offcourt
import tech

import random

print(haus.successMsg)
print(bigshiny.successMsg)
print(inews.successMsg)
print(dcj.successMsg)
print(kino.successMsg)
print(harbinger.successMsg)
print(badandb.successMsg)
print(offcourt.successMsg)
print(tech.successMsg)

# Create playlist list to input into VLC
playlist = []


for x in range(3):
   
    bbObj = {
                'showTitle': badandb.df[x]['showTitle'], 
                'title': badandb.df[x]['title'],
                'url': badandb.df[x]['url'],
                'pubDate' : badandb.df[x]['pubDate']
            }
    bbObj_copy = bbObj.copy()
    playlist.append(bbObj_copy)

    bstObj = {
                'showTitle': bigshiny.df[x]['showTitle'], 
                'title': bigshiny.df[x]['title'],
                'url': bigshiny.df[x]['url'],
                'pubDate' : bigshiny.df[x]['pubDate']
            }
    bstObj_copy = bstObj.copy()
    playlist.append(bstObj_copy)

    dcjObj = {
                'showTitle': dcj.df[x]['showTitle'], 
                'title': dcj.df[x]['title'],
                'url': dcj.df[x]['url'],
                'pubDate' : dcj.df[x]['pubDate']
            }
    dcjObj_copy = dcjObj.copy()
    playlist.append(dcjObj_copy)       

    harbingerObj = {
                'showTitle': harbinger.df[x]['showTitle'], 
                'title': harbinger.df[x]['title'],
                'url': harbinger.df[x]['url'],
                'pubDate' : harbinger.df[x]['pubDate']
            }
    harbingerObj_copy = harbingerObj.copy()
    playlist.append(harbingerObj_copy)

    hausObj = {
                'showTitle': haus.df[x]['showTitle'], 
                'title': haus.df[x]['title'],
                'url': haus.df[x]['url'],
                'pubDate' : haus.df[x]['pubDate']
            }
    hausObj_copy = hausObj.copy()
    playlist.append(hausObj_copy)
        
    inewsObj = {
                'showTitle': inews.df[x]['showTitle'], 
                'title': inews.df[x]['title'],
                'url': inews.df[x]['url'],
                'pubDate' : inews.df[x]['pubDate']
            }
    inewsObj_copy = inewsObj.copy()

    playlist.append(inewsObj_copy)

    kinoObj = {
                'showTitle': kino.df[x]['showTitle'], 
                'title': kino.df[x]['title'],
                'url': kino.df[x]['url'],
                'pubDate' : kino.df[x]['pubDate']
            }
    kinoObj_copy = kinoObj.copy()
    playlist.append(kinoObj_copy)    

    offcourtObj = {
                'showTitle': offcourt.df[x]['showTitle'], 
                'title': offcourt.df[x]['title'],
                'url': offcourt.df[x]['url'],
                'pubDate' : offcourt.df[x]['pubDate']
            }
    offcourtObj_copy = offcourtObj.copy()
    playlist.append(offcourtObj_copy)    

    techObj = {
                'showTitle': tech.df[x]['showTitle'], 
                'title': tech.df[x]['title'],
                'url': tech.df[x]['url'],
                'pubDate' : tech.df[x]['pubDate']
            }
    techObj_copy = techObj.copy()
    playlist.append(techObj_copy)    

   
random.shuffle(playlist)


print('playlist created')
for item in playlist:
    print(item['showTitle'] + " - " + item['title'])
