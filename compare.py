from scipy.signal import hilbert
from scipy.io import wavfile
import numpy as np
import scipy
import sys

def compare(file1, file2):
	sampFreq1, sound1 = wavfile.read(file1)
	sampFreq2, sound2 = wavfile.read(file2)

	snd1 = sound1[:,0]
	snd2 = sound2[:,0]

	if len(snd1) != len(snd2):
		# Determine which array is bigger
		if len(snd1) > len(snd2):
			# Determine how much bigger
			size = len(snd1) - len(snd2)
			snd2 = np.pad(snd2, (0,size), 'constant', constant_values=(0,0)) # Pad with appropriate number of zeros

		elif len(snd1) < len(snd2):
			# Determine how much bigger
			size = len(snd2) - len(snd1)			
			snd1 = np.pad(snd1, (0,size), 'constant', constant_values=(0,0)) # Pad with appropriate number of zeros

	amp_env1 = abs(hilbert(snd1))
	amp_env2 = abs(hilbert(snd2))

	corr = np.corrcoef(amp_env1, amp_env2)[0, 1]
	
	percent = round(corr*100,2)
	
	return percent

if __name__ == "__main__":
	print(compare(sys.argv[1], sys.argv[2]))