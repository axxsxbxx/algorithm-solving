T = int(input())

for _ in range(T):
    num, s = input().split()
    num = int(num)
    for alpha in s:
        print(alpha*num, end='')
    print()