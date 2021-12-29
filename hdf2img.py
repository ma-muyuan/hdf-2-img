"""

.hdf  to  .img

"""

import h5py
import numpy as np
from PIL import Image

class Hdf2Img(object):
	def __init__(self, filename, channel2, channel1=None):
		self.filename = filename
		self.channel1 = channel1
		self.channel2 = channel2

	def read(self):
		with h5py.File(self.filename, 'r') as f:
			if self.channel1 is None:
				self.img_array = np.array(f[self.channel2][:])
			else:
				self.img_array = np.array(f[self.channel1][self.channel2][:])

	def save(self, savepath):
		self.im = Image.fromarray(self.img_array)
		savepath = savepath + '.jpg'
		self.im.convert('RGB').save(savepath)



filename = ''
savename = 'savename'

trans = Hdf2Img(filename, channel2='NOMChannel02')
trans.read()
trans.save(savename)
