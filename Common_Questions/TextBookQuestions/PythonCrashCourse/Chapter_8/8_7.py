'''
8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
 
Use the function to make three dictionaries representing different albums. 
Print each return value to show that the dictionaries are storing the album information correctly.

Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
Make at least one new function call that includes the number of songs on an album.
'''

def make_album(artist,album,NumOfSongs=None):
    complete_album = {'Artist_Name':artist,'Album_Title': album}
    if NumOfSongs:
        complete_album['NumOfSongs'] = NumOfSongs
    else:
        complete_album = {'artist_name':artist,'album_title': album}
    return complete_album

ingest=make_album('timaya','ogologoma',NumOfSongs=19)
print(ingest)

ingest=make_album('bella schmunda',' high tension')
print(ingest)

ingest=make_album('fireboi','Apollo')
print(ingest)

