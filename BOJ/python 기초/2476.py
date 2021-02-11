T = int(input())
prize = []

for _ in range(T):
    numbers = list(map(int, input().split()))
    cnt = [0] * 7

    for num in numbers:
        cnt[num] += 1


    if cnt.count(1) == 3:
        money = max(numbers)*100
    else:
        for i in range(1, 7):
            if cnt[i] == 3:
                money = 10000 + i * 1000
            elif cnt[i] == 2:
                money = 1000 + i * 100
    prize.append(money)
    
print(max(prize))