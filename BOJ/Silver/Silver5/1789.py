n = int(input())
cnt = 0

for i in range(1, n+1):
    if n - i >= 0:
        cnt += 1
    else:
        break
    n -= i

print(cnt)

# while 시용
n = int(input())
cnt = 0
base = 1
while True:
    n -= base
    if n >= 0:
        cnt += 1
        base += 1
    else:
        print(cnt)
        break