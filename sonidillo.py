import numpy as np
import simpleaudio as sa
#import matplotlib.pyplot as plt

# Link:
# https://realpython.com/playing-and-recording-sound-python/

# GLOBAL VARIABLES

bass_cac_de_moun = [210,265,234,171] # sonido como de bass caca de mono
#campanilla = [437.5,875,1180,1422 ] # campanilla fire
#guitarra 
campanilla = [110,220,330,440,550] # guitarrilla osea casi

frequencies = campanilla # this is the list that will be played


fs = 44100  # 44100 samples per second (sample rate)
seconds = 2  # Note duration in seconds
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
    '''TODO: esta linea con sum() se ve fresh, pero creo que la version correcta/segura seria con np.add
    porque el data type es numpy array'''

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
    i = 1 # start counting at one to skip the first step that was created with the
    # get_first_step() function, this is necessary to start with a not empty array
    # and be therefore able to use the numpy concatenate function
    for step in steps:
    # this for-loop was fucked up before, basically in order to iterate over a list
    # follow this guide:
    # https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
        if step and i > 1: # skips first step
            loop = np.concatenate((loop,note))
        elif i > 1:
            loop = np.concatenate((loop,silence))
        i = i + 1

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

def create_track(frequencies,steps): # uses frequencies and steps as inputs
    # not the global variables
    note = create_note(frequencies)
    note = apply_envelope(note)
    loop = create_loop(note,steps)
    return loop

def start_synth():
    note = create_note(frequencies)

    #envelope = np.exp(-t)

    note = apply_envelope(note)

    loop = create_loop(note,steps)

    audio = sanitize_audio(loop)
    
    # 16 steps
    play_audio(audio)

# ----------------------------------------------------------------------------
# --------------- main program -----------------------------------------------
# pvpvpvpv
# start_synth()


# PUTADILLAS DE """""""""""""""""""GUI"""""""""""""""


def cuantos_steps_va_metersh():
    _steps = int(input("Enter Steps: "))
    return _steps

def get_arr(length):
    return [0 for i in range(length)]

def print_steps(_steps):
    s = "|"
    for step in _steps:
        if(step==1):
            s = s + "X|"
        else:
            s = s+ " |"
    print(s)

def get_equicillas(arr, titulo):
    for i in  range(len(arr)):
        print(titulo)
        print_steps(arr)
        arr[i] = int(input("Enter 1 for Step, 0 for Silence: "))
    return arr

# ----------------------------------------------------------------------------
# --------------- pruebillas para hacer tracks--------------------------------
cuantos = cuantos_steps_va_metersh()
stepsCampanilla = get_arr(cuantos)
stepsBass = get_arr(cuantos)


stepsCampanilla = get_equicillas(stepsCampanilla, "Campanas")
stepsBass = get_equicillas(stepsBass , "Bass")


track1 = create_track(campanilla,stepsCampanilla)
track2 = create_track(bass_cac_de_moun,stepsBass)

mixTrack = np.add(track1,track2)
audio = sanitize_audio(mixTrack)

# 16 steps
print_steps(stepsCampanilla)
print_steps(stepsBass)
play_audio(audio)

