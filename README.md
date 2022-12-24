# kun-midi

## Introduction

This is a toy project where the format of storing musical charts (the well-known one being `.midi`) and the interpreter (from charts to audio) are redesigned and implemented from scratch.

A string of text of content:
```
[480]2 2 9= 6= 0 5+ 0 5 0 4= 2 4 5 | 1 1 9= 6= 0 5+ 0 5 0 4= 2 4 5
```
denotes Megalovania, where `480` is the _BPM_ and ` ` and `|` are negligible characters. Pretty self-explainary huh? (Use `b` for ♭)

It shall be noted that the final file format is expected to contain info of mutliple tracks, effects, etc. This string of text shall only be the info of one raw track, one 'line' of the final format. The intial commit just completes an interpreter for lines, which is designed to be a memory-less system. Effects shall be implemented in a separate system.

## Current Work

The final flow should be, a parser reads plain-text track and effect info from a `.kidi` file and feeds them to separate specific parsers (currently `line_to_track.py` is finished as the track part). The processed info is combined to get a _song_ data structure, which is fed to the audio outputter (currently implemented as `song_to_wav.py`) to get the resulting audio.

However as many parts are not finished, for now just
```
python megalovania.py
python arcahv.py
```
to run demos. These two files hard-coded track line info and constructed the _song_ data structure by hand.

---

The name of the project is from [@Gennadiyev](https://github.com/Gennadiyev), a.k.a. The Kunologist
