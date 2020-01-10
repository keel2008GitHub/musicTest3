# coding=utf-8
import os
import string

import matplotlib.pyplot as plt
import librosa
import librosa.display
import librosa.util
import numpy as np
import pandas as pd

totail_beats = 32
number_notes = 24


def frequency_limit(f):
    if f <= 0.9:
        f = 1

    while f > 4186:
        f *= 0.5
    while f < 28:
        f *= 2
    return f


def doScore():
    print("1")
    # In[2]:
    input_wav = os.path.dirname(__file__) + r"/music/recorder.wav"

    y, sr = librosa.load(input_wav, sr=22050, duration=100)

    cent = librosa.feature.spectral_centroid(y=y, sr=sr)

    mod_r = cent[0].shape[0] % number_notes
    cut_count = int(cent[0].shape[0] - mod_r)
    merge_count = int(cut_count / number_notes)

    c = cent[0][:cut_count].reshape(number_notes, merge_count)
    print("2")
    frequencies = []
    notes = []
    for fs in c:
        fm = frequency_limit(fs.mean())
        frequencies.append(fm)
        note = librosa.hz_to_note(fm, octave=True)
        str_list = list(note.replace('#', ''))
        str_list.insert(len(str_list) - 1, '-')
        note = ''.join(str_list)
        notes.append(note.upper())

    unit = (totail_beats / number_notes) - (totail_beats / number_notes) % 0.25
    temp_beat = 4
    print("3")
    i = 0
    beat_summry = 0
    for note in notes:
        if unit * 2 > temp_beat:
            beat_summry += temp_beat
            note = "%s|%.2f" % (note, beat_summry)

            temp_beat = 4
        else:
            temp_beat -= unit
            beat_summry += unit
            note = "%s|%.2f" % (note, beat_summry)
        notes[i] = note
        i += 1

    return notes


# print(doScore())
