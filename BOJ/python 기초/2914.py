song, avg = map(int, input().split())
melody = song * (avg - 1) + 1
print(melody)