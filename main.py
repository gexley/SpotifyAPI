import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="4887508058df48d4bece72506fc4ba01",
                                               client_secret="1514943fc2ba48759e42b00a8812c887",
                                               redirect_uri="https://sites.google.com/potomacschool.org/grant/home",
                                               scope="user-library-read"))

birdy_uri = 'https://open.spotify.com/artist/69VkLw49462xVqUfVdmVMx?si=PeXsB4rMSrO65gkPJ9snqQ'
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])