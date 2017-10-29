from scipy.signal import hilbert
from scipy.io import wavfile
from scipy.stats import variation
import numpy as np
import scipy

def compare(file1, file2):
	snd1 = read_file(file1)
	snd2 = read_file(file2)

	snd1 = resize(snd1)
	snd2 = resize(snd2)

	env1 = amp_env(snd1)
	env2 = amp_env(snd2)
	
	percentage = correlate(env1, env2)
	return percentage

def read_file(file):
	sampFreq, sound = wavfile.read(file)											# Read the file
	snd = sound[:,0]																# Choose one channel of audio to compare
	return snd

def resize2(snd1, snd2):
	if len(snd1) != len(snd2):														# Make arrays the same length
		if len(snd1) > len(snd2):													# Determine which array is bigger
			size_diff = len(snd1) - len(snd2)										# Determine how much bigger
			snd2 = np.pad(snd2, (0,size_diff), 'constant', constant_values=(0,0)) 	# Pad with appropriate number of zeros
			return (snd1, snd2)
		elif len(snd1) < len(snd2):
			size_diff = len(snd2) - len(snd1)										# Determine how much bigger
			snd1 = np.pad(snd1, (0,size_diff), 'constant', constant_values=(0,0))	# Pad with appropriate number of zeros
			return (snd1, snd2)

def resize(snd):
	if len(snd) < 132300:															# Clip the sample to 5 seconds
		size_diff = 132300 - len(snd)												# Determine how much bigger
		snd = np.pad(snd, (0,size_diff), 'constant', constant_values=(0,0))			# Pad with appropriate number of zeros
	elif len(snd) > 132300:
		snd = snd[:132301]
	return snd

def amp_env(snd):
	amp_env = abs(hilbert(snd))														# Find the amplitude envelope
	return amp_env

def correlate(env1, env2):
	corr = np.corrcoef(env1, env2)[0, 1]											# Find the normalized correlation of the envelopes
	percent = round(corr*100,2)														# Round to get percentage
	return percent
