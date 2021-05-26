L, P = map(int, input().split())
newspaper = list(map(int, input().split()))

real_attend = L * P

for people in newspaper:
    print(people - real_attend, end=' ')