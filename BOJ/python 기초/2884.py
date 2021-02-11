h, m = map(int, input().split())

if m >= 45:
    print('{} {}'.format(h, m-45))
else:
    m = m - 45 + 60
    h -= 1
    if h < 0:
        print('{} {}'.format(h+24, m))
    else:
        print('{} {}'.format(h, m))