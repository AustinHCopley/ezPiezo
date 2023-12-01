import adcUtil as adc
import numpy as np
import matplotlib.pyplot as plt
import time

class Piezo:
	def __init__(self, chan=0):
		self.start = 0
		self.chan = chan
		self.data = np.empty(0)
		self.time = np.empty(0)
		self.files = []
		
	def setTime(self, start):
		self.start = start
		
	def read(self):
		piezo = adc.readADC(channel=self.chan)
		self.data = np.append(self.data, piezo)
		self.time = np.append(self.time, time.time() - self.start)
	
	def save(self, name):
		np.savez(f'{name}.npz', self.time, self.data)
		self.files.append(f'{name}.npz')
	
	def plot(self, name):
		npz = np.load(f'{name}.npz')
		time = npz['arr_0']
		data = npz['arr_1']
		
		plt.title(name, fontsize=16)
		plt.xlabel('time')
		plt.ylabel('voltage')
		plt.plot(time, data, 'y')
		plt.legend(['voltage'], fontsize=8)
		plt.show()

def procedure(chord):
	piezo = Piezo()
	input(f'{chord}> ')
	print('recording in...')
	print('3')
	time.sleep(1)
	print('2')
	time.sleep(1)
	print('1')
	time.sleep(1)
	start = time.perf_counter()
	piezo.setTime(start)
	print('start')
	while time.perf_counter() - start < 3:
		piezo.read()
	print('done')
	piezo.save(chord)
	piezo.plot(chord)
	
if __name__ == '__main__':
	
	major = ['AM5', 'BM5', 'CM5', 'DM5', 'EM5', 'FM5', 'GM5']
	# flat root notes denoted with a lowercase:
	majorflat = ['aM5', 'bM5', 'dM5', 'eM5', 'gM5']
	minor = ['Am5', 'Bm5', 'Cm5', 'Dm5', 'Em5', 'Fm5', 'Gm5']
	minorflat = ['am5', 'bm5', 'dm5', 'em5', 'gm5']
	maj7 = ['AM7', 'BM7', 'CM7', 'DM7', 'EM7', 'FM7', 'GM7']
	min7 = ['Am7', 'Bm7', 'Cm7', 'Dm7', 'Em7', 'Fm7', 'Gm7']

	for chord in minor:
		for i in range(3):
			# record multiple variations
			procedure(chord+str(i))
	for chord in major:
		for i in range(3):
			# record multiple variations
			procedure(chord+str(i))

	for chord in maj7:
		for i in range(5): 
			procedure(chord+str(i))
	for chord in min7:
		for i in range(5):
			procedure(chord+str(i))
	
