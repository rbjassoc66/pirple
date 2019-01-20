''' Homework # 7 Dictionaries '''
################## Data ########################
mySong = {'artist':'Neil Diamond',
            'title' :'Red Red Wine',
            'release_year' :1967,
            'genre' :'pop',
            'duration' :'2:42'            
            }

################## Printing Data from Dictioary ####
for k,v in mySong.items():
    print(str(k)+': '  + str(v))
    