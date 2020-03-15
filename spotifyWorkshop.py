import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = ''
CLIENT_SECRET = ''

TB_USER_ID = ''

client_credentials_manager = SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists(TB_USER_ID)

VIBRATIONS_IN_AIR_PL_ID = ''

vib_in_air_tracks = vib_tracks = sp.user_playlist_tracks(TB_USER_ID, playlist_id=VIBRATIONS_IN_AIR_PL_ID)
album_ids = []
count_singles = 0

for track in vib_in_air_tracks['items']:
    album_obj = track['track']['album']

    # did this because i thought Single albums did not have genres... not a true assumption
    if album_obj['album_type'] == u'single':
        count_singles = count_singles + 1
    else:
        album_ids.append(album_obj['id'])

print('count singles: ' + str(count_singles))

# limit for this api req is 20 ids, so take the first 20
albums_of_vib = sp.albums(album_ids[:20])

for album in albums_of_vib['albums']:
    if len(album['genres']) > 0:
        print(album['genres'])
    else:
        print('no genres')
