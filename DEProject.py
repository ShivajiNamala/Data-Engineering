import pymongo
import collections
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient("mongodb://192.168.99.100:27017")

    db = client.dbtwitter
    cursor = db.tbcanada.find()
    
    datalist = []
    langlist = []
    sourcelist = []
    hashlist = []
    followdict = {}
    frdsdict = {}
    coordlist = []
    
    placelist = []
    
    cursor = db.tbcanada.find()
    for document in cursor:
        rowlist = []
        rowlist = [document.get('lang'), document.get('filter_level'),document.get('user')['screen_name'], 
                   document.get('user')['followers_count'], document.get('user')['friends_count'],
                   document.get('user')['favourites_count'], document.get('user')['statuses_count'],
                   document.get('user')['profile_background_color'], 
                   document.get('place')['bounding_box']['coordinates'],
                   document.get('place')['attributes'], document.get('entities')['hashtags'],
                   document.get('source')
                  ]

        datalist.append(rowlist)
        
        langlist.append(document.get('lang')) 
        sourcelist.append(document.get('source')) 
        hashlist.append(document.get('entities')['hashtags']) 
        followdict.update({document.get('user')['screen_name']:document.get('user')['followers_count']})
        frdsdict.update({document.get('user')['screen_name']:document.get('user')['friends_count']})
        coordlist.append(document.get('place')['bounding_box']['coordinates'][0][0])
        placelist.append(document.get('place')['name']) 

#------------------------------------------------------------ 
#----- Top 10 Languages -------------------------------------
#------------------------------------------------------------ 

    counter1=collections.Counter(langlist)

    langtype = []
    langtypecnt = []
    for i,j in counter1.most_common(10):
        langtype.append(i)
        langtypecnt.append(j)
    
    y_pos = np.arange(len(langtype))

    plt.bar(y_pos, langtypecnt, align='center', alpha=0.9, color='#AC34B9')
    plt.xticks(y_pos, langtype)
    plt.ylabel('Users')
    plt.title('Top 10 Languages')

    plt.show()
    
