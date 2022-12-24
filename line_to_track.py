from music_theory import *
import re

r_bracketed = r'\[[^\[\]]*\]'
r_key = r'[0-9][b+]?'
r_note = r'[0-9][b+]?=*'

def line_to_track(line):
    meta_info = re.findall(r_bracketed, line)
    bpm = float(re.sub(r'\[|\]', '', meta_info[0]))
    line = re.sub(r_bracketed, '', line)

    beat = 0
    f = f_table()
    track = []
    notes = re.findall(r_note, line)

    for note in notes:
        length = len(re.sub(r_key, '', note)) + 1
        track.append({
            "f": f[re.search(r_key, note).group()],
            "start": beat_to_time(bpm, beat),
            "end": beat_to_time(bpm, beat + length)
        })
        beat += length
    
    return track