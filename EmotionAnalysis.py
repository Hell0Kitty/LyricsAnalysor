import nltk
from nltk.stem import *
from nltk.corpus import sentiwordnet as swn
import matplotlib.pyplot as plt

def analyze_emotion(inputfile = 'songs.txt'):
	"""analyze_emotion(inputfile) takes the an optional inputfile containing text of lyrics, which is all lyrics by default.
	analyze the positive, negative and objective score of ecah words in the lyrics and plot a respectie pie chart"""

	#Read file, tokenizing and tagging
	fid = open(inputfile,'r')
	contents = fid.read()
	fid.close()
	contents = contents.replace("\n"," ")
	token=nltk.word_tokenize(contents)
	tagged=nltk.pos_tag(token) 
	
	pos_score = 0
	neg_score = 0
	obj_score = 0

	# Using nltk.corpus.sentiwordnet to compute the positivity/negativity of each word. Here I only used the most common meaning of each 		word as a approximation.
	for i in range(0,len(tagged)):
		if 'NN' in tagged[i][1] and len(list(swn.senti_synsets(tagged[i][0],'n')))>0:
			pos_score+=(list(swn.senti_synsets(tagged[i][0],'n'))[0]).pos_score()
			neg_score+=(list(swn.senti_synsets(tagged[i][0],'n'))[0]).neg_score()
			obj_score+=(list(swn.senti_synsets(tagged[i][0],'n'))[0]).obj_score()
		elif 'VB' in tagged[i][1] and len(list(swn.senti_synsets(tagged[i][0],'v')))>0:
			pos_score+=(list(swn.senti_synsets(tagged[i][0],'v'))[0]).pos_score()
			neg_score+=(list(swn.senti_synsets(tagged[i][0],'v'))[0]).neg_score()
			obj_score+=(list(swn.senti_synsets(tagged[i][0],'v'))[0]).obj_score()
		elif 'JJ' in tagged[i][1] and len(list(swn.senti_synsets(tagged[i][0],'a')))>0:
			pos_score+=(list(swn.senti_synsets(tagged[i][0],'a'))[0]).pos_score()
			neg_score+=(list(swn.senti_synsets(tagged[i][0],'a'))[0]).neg_score()
			obj_score+=(list(swn.senti_synsets(tagged[i][0],'a'))[0]).obj_score()
		elif 'RB' in tagged[i][1] and len(list(swn.senti_synsets(tagged[i][0],'r')))>0:
			pos_score+=(list(swn.senti_synsets(tagged[i][0],'r'))[0]).pos_score()
			neg_score+=(list(swn.senti_synsets(tagged[i][0],'r'))[0]).neg_score()
			obj_score+=(list(swn.senti_synsets(tagged[i][0],'r'))[0]).obj_score()
	print("Positive Score is: %f\nNegative Score is: %f\nObjective Score is: %f\n" %(pos_score,neg_score, obj_score))

	#Display Result and Plot the Pie chart.
	labels = 'Positivity', 'Negativity', 'Objectivity'
	sizes = [pos_score,neg_score, obj_score]

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
	ax1.axis('equal')
	plt.show()
	
