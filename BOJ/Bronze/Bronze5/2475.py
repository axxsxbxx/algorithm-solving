a, b, c, d, e = map(int, input().split())

check = a**2 + b**2 + c**2 + d**2 + e**2
ans = check % 10
print(ans)