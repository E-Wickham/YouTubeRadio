import badandb

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

print(playlist)