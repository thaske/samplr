from compare import *
import os

# compare('clap.wav', 'snare.wav')

def main(orig, directory):
	print("Comparing {}".format(orig))
	for filename in os.listdir(directory):
	    if filename.endswith(".wav"): 
	    	file = '{}/{}'.format(directory,filename)
	    	print("{}: {}%".format(filename, compare(orig, file)))

if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])