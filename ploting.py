import numpy as np
import matplotlib
from matplotlib import pyplot
def plot_bar(counts, words):
	
	x = np.arange(20)
	fig, ax = pyplot.subplots()
	ax.bar(x,counts)
	ax.set_xticks(x + 0.35 / 2)
	ax.set_xticklabels(tuple(words), rotation=30)
	pyplot.show()
