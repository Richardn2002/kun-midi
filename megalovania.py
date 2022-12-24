from line_to_track import line_to_track
from song_to_wav import song_to_wav

megalovania = "[480]2 2 9= 6= 0 5+ 0 5 0 4= 2 4 5 | 1 1 9= 6= 0 5+ 0 5 0 4= 2 4 5"

track_0 = line_to_track(megalovania)
song = [{"v": 1, "i": "slap", "notes": track_0}]

song_to_wav(song, "megalovania.wav", 44100)