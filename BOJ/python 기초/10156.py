k, n, m = map(int, input().split())
price = k * n
if price > m:
    print(price - m)
else:
    print(0)