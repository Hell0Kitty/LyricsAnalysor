import numpy as np
import matplotlib
from matplotlib import pyplot


def display_result(counts, words):
	"""display_result(counts, words) takes 20 words and their respective frequency and makes a bar plot"""
	x = np.arange(len(counts))
	fig, ax = pyplot.subplots()
	ax.bar(x,counts)
	ax.set_xticks(x + 0.35 / 2)
	ax.set_xticklabels(tuple(words), rotation=45)
	pyplot.show()
