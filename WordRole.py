import nltk
from nltk.stem import *
import matplotlib.pyplot as plt

def analyze_role(inputfile = 'songs.txt'):
	"""analyze_emotion(inputfile) takes the an optional inputfile containing text of lyrics, which is all lyrics by default.
	analyze the noun, verb, adverb, adjective frequencies and plot a respectie pie chart"""

	#Read file, tokenizing and tagging
	fid = open(inputfile,'r')
	contents = fid.read()
	fid.close()
	contents = contents.replace("\n"," ")
	token=nltk.word_tokenize(contents)
	tagged=nltk.pos_tag(token) 
	
	n_count = 0
	v_count = 0
	adj_count = 0
	adv_count = 0
	p_count = 0
	pre_count = 0
	a_count = 0

	# Using nltk.corpus.sentiwordnet to compute the positivity/negativity of each word. Here I only used the most common meaning of each 		word as a approximation.
	for i in range(0,len(tagged)):
		if 'NN' in tagged[i][1]:
			n_count += 1
		elif 'VB' in tagged[i][1]: 
			v_count += 1
		elif 'PRP' in tagged[i][1]: 
			p_count += 1
		elif 'JJ' in tagged[i][1]:
			adj_count += 1
		elif 'RB' in tagged[i][1]:
			adv_count += 1
		elif 'IN' in tagged[i][1]:
			pre_count += 1
		elif 'DT' in tagged[i][1]:
			a_count += 1
	print("Number of noun is: %f\nNumber of verb is: %f\nNumber of adjctive is: %f\nNumber of adverb is: %f\nNumber of pronoun is: %f\nNumber of preposition is: %f\nNumber of article is: %f\n" %(n_count, v_count, adj_count, adv_count, p_count, pre_count, a_count))

	#Display Result and Plot the Pie chart.
	labels = 'Noun', 'Verb', 'Adjective', 'Adverb', 'Pronoun', 'Preposition', 'Article'
	sizes = [n_count, v_count, adj_count, adv_count, p_count, pre_count, a_count]

	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
	ax1.axis('equal')
	plt.show()

