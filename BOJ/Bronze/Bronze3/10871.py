n, x = map(int, input().split())
numbers = list(map(int, input().split()))
result = []
for num in numbers:
    if num < x:
        result.append(num)
print(*result)