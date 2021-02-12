n = int(input())
base = 2

while base <= n:
    if n % base == 0:
        print(base)
        n /= base
    else:
        base += 1