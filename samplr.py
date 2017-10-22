from scipy.signal import hilbert
from scipy.io import wavfile
import numpy as np
import scipy
import sys
import os


def main(orig, directory):

	print("Comparing {}".format(orig))

	# Loop through folder to compare
	for filename in os.listdir(directory):

	    # Filter out only .wav files
	    if filename.endswith(".wav"): 

	    	# Get the path name to the files
	    	file = '{}/{}'.format(directory,filename)

	    	# Print the percentages
	    	print("{}: {}%".format(filename, compare(orig, file)))


def compare(file1, file2):

	# Read the files
	sampFreq1, sound1 = wavfile.read(file1)
	sampFreq2, sound2 = wavfile.read(file2)

	# Choose one channel of audio to compare
	snd1 = sound1[:,0]
	snd2 = sound2[:,0]

	# Make arrays the same length
	if len(snd1) != len(snd2):

		# Determine which array is bigger
		if len(snd1) > len(snd2):

			# Determine how much bigger
			size_diff = len(snd1) - len(snd2)
			# Pad with appropriate number of zeros
			snd2 = np.pad(snd2, (0,size_diff), 'constant', constant_values=(0,0))

		elif len(snd1) < len(snd2):

			# Determine how much bigger
			size_diff = len(snd2) - len(snd1)
			# Pad with appropriate number of zeros
			snd1 = np.pad(snd1, (0,size_diff), 'constant', constant_values=(0,0))

	# Find the amplitude envelope
	amp_env1 = abs(hilbert(snd1))
	amp_env2 = abs(hilbert(snd2))

	# Correlate the envelopes
	corr = np.corrcoef(amp_env1, amp_env2)[0, 1]

	# Round to get percentage
	percent = round(corr*100,2)	
	return percent


if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])