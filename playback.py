import numpy as np
import simpleaudio as sa

frequency = 440  # Our played note will be 440 Hz
fs = 44100  # 44100 samples per second
seconds = 6  # Note duration of 3 seconds

# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * fs, False)

# Generate a 440 Hz sine wave
note = np.sin(frequency * t * 2 * np.pi) + np.sin(2.7*frequency * t * 2 * np.pi)

envelope = np.exp(-t)

note2 = np.multiply(note,envelope) # element-wise multiplication

# Ensure that highest value is in 16-bit range
audio = note2 * (2**15 - 1) / np.max(np.abs(note2))
# Convert to 16-bit data
audio = audio.astype(np.int16)


# Start playback
play_obj = sa.play_buffer(audio, 1, 2, fs)

# Wait for playback to finish before exiting
play_obj.wait_done()
