from instruments import instruments
import wave
import struct

def song_to_wav(song, filename, SAMPLE_RATE = 8000):
    end_times = [max(track["notes"], key = lambda x: x["end"])["end"] for track in song["tracks"]]
    song_len = max(end_times)
    n_frames = int(song_len * SAMPLE_RATE)

    wav_file = wave.open(filename, "w")
    wav_file.setparams((
        1, 2, SAMPLE_RATE, n_frames, "NONE", "not compressed"
    ))

    for tick in range(n_frames):
        t = tick / SAMPLE_RATE
        sample = 0

        for track in song["tracks"]:
            v = track["v"]
            i = instruments[track["i"]]
            for note in track["notes"]:
                if note["f"] == 0: continue
                if t >= note["start"] and t < note["end"]:
                    sample += v * i(note["f"], t - note["start"])
        
        wav_file.writeframes(struct.pack('h', int(sample)))

    wav_file.close()