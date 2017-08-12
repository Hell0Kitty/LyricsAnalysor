import requests
from DataCollection import download_tracks, download_albums, download_lyrics
from Stemming import stem_lyrics
from EmotionAnalysis import analyze_emotion

#MusixMatch URL and API key
base_url = 'http://api.musixmatch.com/ws/1.1/'
apikey = '&apikey=3f1a9f46e6871d50ad6da1960f5723df'

def analyze_artist_lyrics():
	artist = input("Please input artist's first name: \n")
	artist = artist.lower()
	artist_json = requests.get(base_url + 'artist.search?q_artist=' + artist + apikey)
	artist_json = artist_json.json()
	if artist_json['message']['header']['status_code'] == 200:
		artists_list = artist_json["message"]["body"]["artist_list"]
		if len(artists_list) > 0:
			fid = open('songs.txt', 'w')
			fid.close()
			fid = open('songs_list.txt', 'w')
			fid.close()
			fid = open('artists_songs.txt','w')
			fid.write(str(artists_list[0]['artist']['artist_id']) + '\n')
			fid.close()
			name = artists_list[0]['artist']['artist_name']
			download_albums(inputfile = 'artists_songs.txt', outputfile = 'artists_songs.txt') 
			download_tracks(inputfile = 'artists_songs.txt', outputfile = 'artists_songs.txt') 
			holder = 0;
			download_lyrics(holder, inputfile = "artists_songs.txt")
			print("Analyze songs for %s" %name)
			stem_lyrics()
			analyze_emotion()
		else: 
			print("Artist Not found!\n")


	else: 
		print("Error getting response!")


 
