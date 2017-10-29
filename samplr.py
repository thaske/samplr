# -*- coding: utf-8 -*-
from compare import *
import sys
import os

def main(orig, directory):
	print("Comparing {}".format(orig))
	for filename in os.listdir(directory):							# Loop through folder to compare
	    if filename.endswith(".wav"): 								# Filter out only .wav files
	    	file = '{}/{}'.format(directory,filename)				# Get the path name to the files
	    	print("{}: {}%".format(filename, compare(orig, file)))	# Print the percentages

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])