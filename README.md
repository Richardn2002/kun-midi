# kun-midi

This is a toy project where the format of storing musical charts (the well-known one being `.midi`) and the interpreter (from charts to audio) are redesigned and implemented from scratch.

A string of text of content:
```
[480]2 2 9= 6= 0 5+ 0 5 0 4= 2 4 5 | 1 1 9= 6= 0 5+ 0 5 0 4= 2 4 5
```
denotes Megalovania, where `480` is the _BPM_ and ` ` and `|` are negligible characters. Pretty self-explainary huh? (Use `b` for ♭)

It shall be noted that the final file format is expected to contain info of mutliple tracks, effects, etc. This string of text shall only be the info of one raw track, one 'line' of the final format. The intial commit just completes an interpreter for lines, which is designed to be a memory-less system. Effects shall be implemented in a separate system.

---

The name of the project is from [@Gennadiyev](https://github.com/Gennadiyev), a.k.a. The Kunologist
