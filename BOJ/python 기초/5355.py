T = int(input())

for _ in range(T):
    cal = input().split()
    num = float(cal[0])

    for i in range(1, len(cal)):
        if cal[i] == '@':
            num *= 3
        elif cal[i] == '%':
            num += 5
        elif cal[i] == '#':
            num -= 7

    print('{0:.2f}'.format(num))