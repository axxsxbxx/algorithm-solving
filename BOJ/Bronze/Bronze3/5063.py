T = int(input())

for _ in range(T):
    r, e, c = map(int, input().split())
    benefit = e - c
    if r < benefit:
        print('advertise')
    elif r > benefit:
        print('do not advertise')
    else:
        print('does not matter')