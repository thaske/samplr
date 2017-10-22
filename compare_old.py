from scipy.signal import hilbert
from scipy.io import wavfile
import numpy as np
import scipy

def compare(file1, file2):
	sampFreq1, sound1 = wavfile.read(file1)											# Read the files
	sampFreq2, sound2 = wavfile.read(file2)
	snd1 = sound1[:,0]																# Choose one channel of audio to compare
	snd2 = sound2[:,0]
	if len(snd1) != len(snd2):														# Make arrays the same length
		if len(snd1) > len(snd2):													# Determine which array is bigger
			size_diff = len(snd1) - len(snd2)										# Determine how much bigger
			snd2 = np.pad(snd2, (0,size_diff), 'constant', constant_values=(0,0))	# Pad with appropriate number of zeros
		elif len(snd1) < len(snd2):
			size_diff = len(snd2) - len(snd1)										# Determine how much bigger
			snd1 = np.pad(snd1, (0,size_diff), 'constant', constant_values=(0,0))	# Pad with appropriate number of zeros
	amp_env1 = abs(hilbert(snd1))													# Find the amplitude envelope
	amp_env2 = abs(hilbert(snd2))
	corr = np.corrcoef(amp_env1, amp_env2)[0, 1]									# Find the normalized correlation of the envelopes
	percent = round(corr*100,2)														# Round to get percentage
	return percent