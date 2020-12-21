def make_album(artist,album,NumOfSongs=None):
    complete_album = {'Artist_Name':artist,'Album_Title': album}
    if NumOfSongs:
        complete_album['NumOfSongs'] = NumOfSongs
    else:
        complete_album = {'artist_name':artist,'album_title': album}
    return complete_album