from line_to_track import line_to_track
from song_to_wav import song_to_wav

arcahv = "[200]5===7b=8=9==5=7b4+2b+1+===7b===6==22=7b6===5====0==5=7b89===8====4+==2b+1+===7b="

track_0 = line_to_track(arcahv)
song = {
    "tracks": [
        {"v": 0.5, "i": "sine", "notes": track_0}
    ],
    "effects": []
}

song_to_wav(song, "arcahv.wav")