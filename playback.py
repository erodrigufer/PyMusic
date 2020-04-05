import numpy as np
import simpleaudio as sa
#import matplotlib.pyplot as plt


# Link:
# https://realpython.com/playing-and-recording-sound-python/

frequency = 440  # Our played note will be 440 Hz
fs = 44100  # 44100 samples per second (sample rate)
seconds = 5  # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)

# Generate a 440 Hz sine wave
#note = np.sin(frequency * t * 2 * np.pi) + np.sin(2.7*frequency * t * 2 * np.pi)

#note3 = np.sin(1.7*frequency * t * 2 * np.pi)

note = np.sin(437.5 * t * 2 * np.pi) + np.sin(875 * t * 2 * np.pi) + np.sin(1180 * t * 2 * np.pi) + np.sin(1422 * t *2 * np.pi) # frecuencias de la campanilla

#note = np.sin(101.6 * t * 2 * np.pi)+ np.sin(171.9 * t * 2 * np.pi)+ np.sin(210 * t * 2 * np.pi) +  np.sin(265 * t * 2 * np.pi) #sonidillo de tambor

#plt.plot(note3)
#plt.show()

envelope = np.exp(-t)
#envelope = 1

note2 = np.multiply(note,envelope) # element-wise multiplication

# Ensure that highest value is in 16-bit range
audio = note2 * (2**15 - 1) / np.max(np.abs(note2))
# Convert to 16-bit data
audio = audio.astype(np.int16)

#audio2 = note3 * (2**15 - 1) / np.max(np.abs(note3))
#audio2 = audio2.astype(np.int16)


# Start playback
play_obj = sa.play_buffer(audio, 1, 2, fs)

# Wait for playback to finish before exiting
play_obj.wait_done()

#play_obj = sa.play_buffer(audio2, 1, 2, fs)
#play_obj.wait_done()

