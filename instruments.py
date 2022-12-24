from music_theory import f_table

import numpy as np
from scipy import signal
from scipy.io import wavfile

def sine(f, t):
    return 32767.0 * np.sin(2 * np.pi * f * t)

def saw(f, t):
    return 32767.0 * signal.sawtooth(2 * np.pi * f * t)

def triangle(f, t):
    return 32767.0 * signal.sawtooth(2 * np.pi * f * t, 0.5)

def square(f, t):
    return 32767.0 * signal.square(2 * np.pi * f * t, 0.5)

rate, data = wavfile.read("soundfonts/2022-12-23-14-52-2-1.wav")
ams_grand_piano_harp_info = {
    "rate": rate,
    "data": data,
    "freq": f_table()["1"],
    "loop_start": 32264,
    "loop_len": 33612 - 32264
}
def ams_grand_piano_harp(f, t):
    info = ams_grand_piano_harp_info

    k = t * info["rate"] * f / info["freq"]

    if k > info["loop_start"]:
        k = info["loop_start"] + (k - info["loop_start"]) % info["loop_len"]
    
    i = int(k)
    return (k-i) * info["data"][i+1] + (i+1-k) * info["data"][i]

rate, data = wavfile.read("soundfonts/Bass/242-a11.wav")
slap_bass_info = {
    "rate": rate,
    "data": data,
    "freq": f_table(220)["1"],
    "loop_start": 27385,
    "loop_len": 28206 - 27385
}
def slap_bass(f, t):
    info = slap_bass_info

    k = t * info["rate"] * f / info["freq"]

    if k > info["loop_start"]:
        k = info["loop_start"] + (k - info["loop_start"]) % info["loop_len"]
    
    i = int(k)
    return (k-i) * info["data"][i+1] + (i+1-k) * info["data"][i]

instruments = {
    "sine": sine,
    "saw": saw, 
    "tri": triangle,
    "sqr": square,
    "piano": ams_grand_piano_harp,
    "slap": slap_bass
}