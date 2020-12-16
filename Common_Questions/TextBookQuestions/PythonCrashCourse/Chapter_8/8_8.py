'''
8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
Be sure to include a quit value in the while loop.
'''


def make_album(artist,album,NumOfTracks=None):
    completed_album = {'artist_name':artist,'album_title':album}
    if NumOfTracks:
        completed_album['NumOfTracks']=NumOfTracks
        return completed_album
    else:
        completed_album = {'artist_name':artist,'album_title':album}
    print(completed_album)

while True:
    artist_name=input('Enter artist name: ')
    if artist_name == 'quit':
        break
    artist_title=input('Enter the album title: ')
    if artist_title=='quit':
        break
    make_album(artist_name,artist_title)



'''
This will give you a different outcome

    if artist_name == 'quit' or artist_title=='quit':
        break

'''