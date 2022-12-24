import requests
from requests.exceptions import HTTPError
import sys

albums = ["taylor swift", "fearless", "speak now", "red", "1989", "lover", "reputation", "folklore", "evermore", "midnights"]

album_or_song = ""
if len(sys.argv) - 1:
    album_or_song = sys.argv[1]

if(not len(album_or_song)):
    url = "https://taylorswiftapi.onrender.com/get"
elif(album_or_song.lower() in albums):
    url = f"https://taylorswiftapi.onrender.com/get?album={album_or_song}"
else:
    url = f"https://taylorswiftapi.onrender.com/get?song={album_or_song}"
    
try:
    response = requests.get(url)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}', file=sys.stderr)
    exit(1)
except Exception as err:
    print(f'error occurred: {err}', file=sys.stderr)
    exit(1)

lyric = response.json()['quote']
print(lyric, file=sys.stdout)
