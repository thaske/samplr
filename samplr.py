from scipy.signal import hilbert
from scipy.io import wavfile
import numpy as np
import scipy
sampFreq1, snd1 = wavfile.read('clap.wav')
sampFreq2, snd2 = wavfile.read('clap2.wav')
amp_env1 = abs(hilbert(snd1[:, 0]))
amp_env2 = abs(hilbert(snd2[:, 0]))
corr = np.corrcoef(amp_env1, amp_env2)[0, 1]
print('Similarity: {:.2f}%'.format(corr*100))