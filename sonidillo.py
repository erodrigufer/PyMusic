import numpy as np
import simpleaudio as sa
#import matplotlib.pyplot as plt

# Link:
# https://realpython.com/playing-and-recording-sound-python/

# GLOBAL VARIABLES

bass_cac_de_moun = [210,265,234,171] # sonido como de bass caca de mono
campanilla = [437.5,875,1180,1422 ] # campanilla fire
frequencies = campanilla
fs = 44100  # 44100 samples per second (sample rate)
seconds = 2  # Note duration of 3 seconds
pi = np.pi
steps = [ 0 if i%2 != 0 else 1 for i in range(16)]
t = np.linspace(0, seconds, seconds * fs, False) # Generate array with seconds*sample_rate steps, ranging between 0 and seconds


# METHODS

# Creates sine wave with specific frequency
def generate_wave(frequency):
    return np.sin(frequency * t * 2 * pi)

# Adds a sine wave from each frequency in frequencies
def create_note(frequencies):
    return sum([generate_wave(frequency) for frequency in frequencies]) 

# Creates envelope with exponential function to apply to note
def create_envelope():
    return np.exp(-t)

def apply_envelope(note):
    return np.multiply(note,create_envelope()) # element-wise multiplication

def get_first_step(note, step):
    if step:
        return note
    else:
        return generate_wave(0)

def create_loop(note, steps):
    
    silence = generate_wave(0)
    
    loop = get_first_step(note,steps[0])

    for step in range(1,len(steps)):
        if step:
            loop = np.concatenate((loop,note))
        else:
            loop = np.concatenate((loop,silence))
    return loop

def sanitize_audio(loop):
    # Ensure that highest value is in 16-bit range
    audio = loop * (2**15 - 1) / np.max(np.abs(loop))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)
    return audio

def play_audio(audio):
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    # Wait for playback to finish before exiting
    play_obj.wait_done()


def start_synth():
    note = create_note(frequencies)

    #envelope = np.exp(-t)

    note = apply_envelope(note)

    loop = create_loop(note,steps)

    audio = sanitize_audio(loop)
    
    # 16 steps
    play_audio(audio)

# pvpvpvpv
start_synth()

