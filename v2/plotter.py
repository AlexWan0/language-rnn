import os
from matplotlib import pyplot as plt

class Plotter():
	def __init__(self):
		self.stats = {}

	def add(self, **kwargs):
		for k, v in kwargs.items():
			if k not in self.stats:
				self.stats[k] = []

			self.stats[k].append(v)

	def build_plot(self, suptitle=None, subplots=None, figsize=(10, 10), **kwargs):
		if subplots == None:
			fig, ax = plt.subplots(1, len(self.stats), figsize=figsize)
		else:
			fig, ax_array = plt.subplots(*subplots, figsize=figsize)
			ax = ax_array.flatten()

		if suptitle != None:
			fig.suptitle(suptitle)

		for i, (k, v) in enumerate(self.stats.items()):
			ax[i].plot(v, label=k, **kwargs)

			ax[i].legend(loc="upper left")

	def output(self, suptitle=None, subplots=None, figsize=(10, 10), **kwargs):
		self.build_plot(suptitle=suptitle, subplots=subplots, figsize=figsize, **kwargs)

		plt.savefig(fp)
		plt.close()

	def output_show(self, suptitle=None, subplots=None, figsize=(10, 10), **kwargs):
		self.build_plot(suptitle=suptitle, subplots=subplots, figsize=figsize, **kwargs)

		plt.show()

class RunningAvg:
	def __init__(self, buffer_size, default=None):
		self.buffer = [default] * buffer_size
		self.idx = 0
		self.buffer_size = buffer_size
	
	def __call__(self, x):
		self.buffer[self.idx] = x
		self.idx = (self.idx + 1) % self.buffer_size
		return self.none_avg()
	
	def none_avg(self):
		return sum([b for b in self.buffer if b != None]) / self.buffer_size
