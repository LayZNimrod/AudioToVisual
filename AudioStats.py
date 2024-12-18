import librosa
import numpy
timeSeries, sampleRate = librosa.load("El Huervo - A Thing With Feathers - 06 Romania.flac")

# getting a matrix which contains amplitude values according to frequency and time indexes
stft = numpy.abs(librosa.stft(timeSeries, hop_length=512, n_fft=2048*4))# converting the matrix to decibel matrix
spectrogram = librosa.amplitude_to_db(stft, ref=numpy.max)

frequencies = librosa.core.fft_frequencies(n_fft=2048*4)


