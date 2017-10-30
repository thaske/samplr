# -*- coding: utf-8 -*-
from compare import *
import sys
import os

def main(orig, directory):
	print("Comparing {}".format(orig))

	# Loop through folder to compare
	for filename in os.listdir(directory):

		# Filter out only .wav files
	    if filename.endswith(".wav"):

	    	# Get the path name to the files
	    	file = '{}/{}'.format(directory, filename)

	    	# Print the percentages
	    	print("{}: {}%".format(filename, compare(orig, file)))

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])