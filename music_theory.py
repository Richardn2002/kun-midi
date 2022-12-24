INTERVAL = 2 ** (1 / 12)

def beat_to_time(bpm, beat):
    return beat / bpm * 60

def f_table(mid_C = 440 / INTERVAL ** 9):
    table = {"0": 0}

    f = mid_C / INTERVAL

    for notes in [
        ["1b"],
        ["1"],
        ["1+", "2b"],
        ["2"],
        ["2+", "3b"],
        ["3", "4b"],
        ["3+", "4"],
        ["4+", "5b"],
        ["5"],
        ["5+", "6b"],
        ["6"],
        ["6+", "7b"],
        ["7", "8b"],
        ["7+", "8"],
        ["8+", "9b"],
        ["9"],
        ["9+"]
    ]:
        for note in notes:
            table[note] = f
        f *= INTERVAL

    return table