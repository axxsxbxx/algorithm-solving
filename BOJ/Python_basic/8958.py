T = int(input())
for _ in range(T):
    cnt = 0
    score = 0
    ans = input()
    for result in ans:
        if result == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)