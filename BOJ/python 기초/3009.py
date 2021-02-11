x, y = [], []
for _ in range(3):
    a, b = input().split()
    x.append(a)
    y.append(b)

m, n = 0, 0
for i in range(3):
    if x.count(x[i]) == 1:
        m = x[i]
        break
for i in range(3):
    if y.count(y[i]) == 1:
        n = y[i]
        break
print('{} {}'.format(m, n))