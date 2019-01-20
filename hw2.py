
''' Homework # 2 Functions '''
################## Variables ########################

artist = 'Neil Diamond'
title = 'Red Red Wine'
release_year = 1967
genre = 'pop'
duration = '2:42'

def fArtist():
    return artist

def fTitle():
    return title

def fReleaseYear():
    return release_year

def fgenre():
    return genre

def fDuration():
    return duration

def aTest():
    if artist == 'Neil Diamond':
        return True


print(fArtist())
print(fTitle())
print(fReleaseYear())
print(fgenre())
print(fDuration())

############ extra credit #############

print('this is extra credit', aTest())


