from scipy.signal import hilbert
from scipy.io import wavfile
import soundfile as sf
import numpy as np
import scipy

def compare(file1, file2):
	snd1 = read_file2(file1)
	snd2 = read_file2(file2)

	snd1 = resize(snd1)
	snd2 = resize(snd2)

	env1 = amp_env(snd1)
	env2 = amp_env(snd2)

	percentage = correlate(env1, env2)
	return percentage

def scompare(env1, env2):
	percentage = correlate(env1, env2)
	return percentage

def get_env(file):
	snd = read_file(file)
	snd = resize(snd)
	env = amp_env(snd)
	return env

def read_file2(file):
	# Read the file
	sound, sampFreq = sf.read(file)
	# Choose one channel of audio to compare
	snd = sound[:,0]
	return snd

def read_file(file):
	# Read the file
	sampFreq, sound = wavfile.read(file)
	# Choose one channel of audio to compare
	snd = sound[:,0]
	return snd

def resize2(snd1, snd2):
	# Make arrays the same length
	if len(snd1) != len(snd2):
		# Determine which array is bigger
		if len(snd1) > len(snd2):
			# Determine how much bigger
			size_diff = len(snd1) - len(snd2)
			# Pad with appropriate number of zeros
			snd2 = np.pad(snd2, (0,size_diff), 'constant', constant_values=(0,0))
			return (snd1, snd2)
		elif len(snd1) < len(snd2):
			# Determine how much bigger
			size_diff = len(snd2) - len(snd1)
			# Pad with appropriate number of zeros
			snd1 = np.pad(snd1, (0,size_diff), 'constant', constant_values=(0,0))
			return (snd1, snd2)

def resize(snd):
	# Clip the sample to 5 seconds 220500
	if len(snd) < 220500:
		# Determine how much bigger
		size_diff = 220500 - len(snd)
		# Pad with appropriate number of zeros
		snd = np.pad(snd, (0, size_diff), 'constant', constant_values=(0,0))
	elif len(snd) > 220500:
		snd = snd[:220501]
	return snd

def amp_env(snd):
	# Find the amplitude envelope
	# amp_env = abs(hilbert(snd)).tolist()
	amp_env = abs(hilbert(snd))
	return amp_env

def correlate(env1, env2):
	# Find the normalized correlation of the envelopes
	corr = np.corrcoef(env1, env2)[0, 1]
	# Round to get percentage
	percent = round(corr*100,2)
	return percent
