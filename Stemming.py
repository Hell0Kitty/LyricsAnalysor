import nltk.stem
import matplotlib
import numpy as np
from nltk.stem.porter import * 
from matplotlib import pyplot
import operator
from Visualization import display_result

def preproc(body):
	"""preproc(body) takes the body of the lyrics json response. It stores the raw data in 'songs_list.txt' and the 
	trimmed lyrics in 'songs.txt' """
	#store raw data to 'songs_list.txt'
	import string
	import re
	outputfile1 = "songs_list.txt"
	fid = open(outputfile1, 'a')
	fid.write(body+'\n')
	fid.close()

	#store trimmed lyrics to 'songs.txt'
	outputfile = 'songs.txt'
	body = body.replace('\\n',' ')
	body = re.sub('\*\*\*\*\*\*\*+.*', '',body)
	body = re.sub('\([0-9]+\)', '',body)
	body = re.sub('\'', 'XXXCOMMAXXX', body)
	body = re.sub('[%s]' %re.escape(string.punctuation), '',body)
	body = re.sub('XXXCOMMAXXX', '\'', body)
	fid2 = open(outputfile,'a')
	fid2.write(body + '\n')
	fid2.close


def stem_lyrics():
	"""stem_lyrics() stem the words in lyrics file 'songs.txt' using nltk stemmer. It counts the frequency of the stemmed words
 	and calls the display_result function to visualize the results. """
	
	#Stemming
	fid = open('songs.txt','r')
	contents = fid.read()
	fid.close()
	contents = contents.replace("\n"," ")
	contents = contents.split()
	stemmer = PorterStemmer()
	
	#Word Counting
	word_counter = dict()
	for word in contents:
		if(len(word) > 0):
			word = stemmer.stem(word)
			if(word in word_counter):
				word_counter[word] = word_counter[word] + 1
			else:
				word_counter[word] = 1
	top = sorted(word_counter.items(), key=operator.itemgetter(1), reverse = True)
	
	#Visualization
	for i in range(10):
		if (i + 1) * 20 < len(top):
			fraction = top[i * 20 : (i + 1) * 20]
			d = dict(fraction)
			words = np.array(list(d.keys()))
			counts = np.array(list(d.values()))
			display_result(counts, words)
		else:
			if i * 20 < len(top):
				fraction = top[i * 20 : len(top)]
				d = dict(fraction)
				words = np.array(list(d.keys()))
				counts = np.array(list(d.values()))
				display_result(counts, words)

