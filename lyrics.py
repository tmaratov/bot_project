from genius import Genius
import requests
import json

g = Genius(access_token="HcAgpKN4LvM3-BkegBAT2qYW_nPiiQ2PEAv5Nt4KU4l2CrwET91NrfiyhUbIkg2z")

artist = 'Kendrick Lamar' #input('>> name of artist ')
song = 'LOVE' #input('>> name of song ')
token = 'YmyXNq15z-RRysYsaAIdnaIuJLmrWTy_KRHXpXl1UrS1MYvDVof9oKoEZuN2V4We'

artist = g.search_artist(artist)
url = 'https://api.genius.com/search?='
headers = {'Authorization': "Bearer " + token}
data = {'q': song}
response = requests.get(url, headers=headers, params=data)

if response.status_code == 200:
    data = response.json()

    
    for hit in data["response"]["hits"]:
        if hit["result"]["primary_artist"]["name"] == artist:
            song_info = hit
            break
        print(song_info)
            # if hit["result"]["title"] == song:
            #     print(hit["result"]["id"])
            #     id_of_song = hit["result"]["id"]






# for songs in artist.songs_by_popularity:
    # print(songs)
    # songs = songs.split('(')
    # print(songs)
    # if song == songs[0]:
    #     print(song)



song = g.get_song(song_id=id_of_song)
print(song.title_with_featured)
print(song.release_date_for_display)

#print(song.album)
#for featured in song.features:
#    print(featured.name)

# lyrics = song.lyrics
# print('\n'.join(lyrics))