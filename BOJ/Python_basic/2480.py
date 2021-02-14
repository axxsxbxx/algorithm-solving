numbers = list(map(int, input().split()))
cnt = [0] * 7

for num in numbers:
    cnt[num] += 1


if cnt.count(1) == 3:
    print(max(numbers)*100)
else:
    for i in range(1, 7):
        if cnt[i] == 3:
            print(10000 + i * 1000)
        elif cnt[i] == 2:
            print(1000 + i * 100)

