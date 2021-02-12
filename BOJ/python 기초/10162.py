time = int(input())
base = [300, 60, 10]
cook = []
if time % 10 != 0:
    print(-1)
else:
    while time > 0:
        for n in base:
            cook.append(time // n)
            time -= n * (time // n)
    print(*cook)