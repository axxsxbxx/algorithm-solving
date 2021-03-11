from math import floor

n1, n2, n12 = map(int, input().split())

N = floor((n1 + 1) * (n2 + 1) / (n12 + 1) - 1)
print(N)