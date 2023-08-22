def make_album(artist, album_title, songs=None):
    '''return dictionary of a music album'''

    if songs:
        album = {'artist': artist, 'album': album_title, 'songs': songs, }
        return album
    else:
        album = {'artist': artist, 'album': album_title, }
        return album


print("Press q to quite at any time.")

while True:
    artist = input("Please enter an artist: ")
    if artist == 'q':
        break
    album = input("Please enter an album from the artist: ")
    if album == 'q':
        break
    print(make_album(artist, album))


# print(make_album('deftones', 'around the fur'))
# print(make_album('deftones', 'white pony', 12))
# print(make_album('deftones', 'adrenaline'))
