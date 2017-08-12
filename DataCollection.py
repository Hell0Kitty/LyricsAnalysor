import requests
from Stemming import preproc
#MusixMatch URL and API key
base_url = 'http://api.musixmatch.com/ws/1.1/'
apikey = '&apikey=3f1a9f46e6871d50ad6da1960f5723df'

def download_artists( outputfile = "artists_list.txt"):
	"""download_artists() takes an optional input outputfile to specify where to write the result. 
	It retrives the artists ID od the 100 most famous artists ID (in MusixMatch Database)
	in United States and stores them in the outputfile, which is 'artists_lists.txt' by default"""
 
	artists = requests.get(base_url + 'chart.artists.get?page=1&page_size=100' + apikey)
	artists = artists.json()
	artists_list = artists["message"]["body"]["artist_list"]

	fid = open(outputfile,'w')
	for i in range(0,len(artists_list)):
		fid.write(str(artists_list[i]['artist']['artist_id']) + '\n')

	fid.close()



def download_albums(inputfile = "artists_list.txt", outputfile = "albums_list.txt"):
	"""download_albums(inputfile, outputfile) takes the an optional inputfile containing artisits IDs, and an optional 
	outputfile to write the albums ID to. It retreives all albums IDs for each artist ID in the inputfile, and write the 
	result to outputfile, which is by default 'albums_lists.txt' """
	
	with open(inputfile) as fid:
		content = fid.readlines()
	content = [x.strip() for x in content]
	fid.close()

	print("Sending HTTP requests......\n")
	count = 1

	fid = open(outputfile,'w')
	for i in range(0,len(content)):
		print("% " + str(100 * count/len(content)) + " sent......\n")
		artist_id = content[i]
		albums_list = requests.get(base_url + "artist.albums.get?s_release_date=desc&g_album_name=1" + apikey + "&artist_id=" + artist_id)
		albums_list = albums_list.json()
		albums_list = albums_list["message"]["body"]["album_list"]
		for j in range(0,len(albums_list)):
			album = albums_list[j]["album"]["album_id"]
			fid.write(str(album) + '\n')
		count = count + 1 

	fid.close()



def download_tracks(inputfile = "albums_list.txt", outputfile = "tracks_list.txt"):
	"""download_albums(inputfile, outputfile) takes the an optional inputfile containing albums IDs, and an optional 
	outputfile to write the tracks ID to. It retreives all tracks IDs for each albums ID in the inputfile, and write the 
	result to outputfile, which is by default 'tracks_lists.txt' """

	with open(inputfile) as fid:
		content = fid.readlines()
	content = [x.strip() for x in content]
	fid.close()

	print("Sending HTTP requests......\n")
	count = 1

	fid = open(outputfile,'w')
	for i in range(0,len(content)):
		print("% " + str(count * 100 / len(content)) + " sent......\n")
		album_id = content[i]
		tracks_list = requests.get(base_url + "album.tracks.get?page_size=100" + apikey + "&album_id=" + album_id)
		tracks_list = tracks_list.json()
		tracks_list = tracks_list["message"]["body"]["track_list"]
		for j in range(0,len(tracks_list)):
			track = tracks_list[j]["track"]["track_id"]
			fid.write(str(track) + '\n')
		count = count + 1 

	fid.close()




def download_lyrics(*args, inputfile = "tracks_list.txt", countfile = "count.txt"): 

	"""download_lyrics(inputfile, countfile) takes the an optional inputfile containing tracks IDs, and an optional 
	countfile which keeps track of the previous process, due to the MusixMatch API's API call constraint. Passing any 
	additional argument will inhibit the use of countfile mechanism, assuming the API is not limited. It retreives
	lyrics for all tracks ID in the inputfile, can the function preproc() to store and preprocess the lyrics  """


	with open(inputfile) as fid:
		content = fid.readlines()
	content = [x.strip() for x in content]
	fid.close()

	if len(args) == 0:
		fid = open(countfile,'r')
		count = fid.read()
		fid.close()
		count = int(count)
	else:
		count = 0

	print("Processing ... \n")
	progress = 0
	pseudo_count = count
	#Get the Json response and call preproc() to preprocess the body of each response
	for i in range(count,count + 1600):
		print("Downloading process %d/ %d ......\n" %(progress, min(len(content) - pseudo_count, 1600)))
		if count < len(content):
			track_id = content[i]
			tracks_lyrics = requests.get(base_url + "track.lyrics.get?" + apikey + "&track_id=" + track_id)
			tracks_lyrics = tracks_lyrics.json()
			if tracks_lyrics['message']['header']['status_code'] == 200:
				body = tracks_lyrics["message"]["body"]["lyrics"]["lyrics_body"]
				preproc(body)
			else:
				print("Error getting lyrics %i \n" %count)
			count = count + 1
		else: 
			break
		progress = progress + 1
	
	if len(args) == 0:
		fid = open(countfile,'w')
		fid.write(str(count))
		fid.close()


