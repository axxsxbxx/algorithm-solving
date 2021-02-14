T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    small, big, result = 0, 0, 0
    if a >= b:
        small = a
        big = b
    else:
        small = b
        big = a
    for i in range(2, small+1):
        if small % i == 0 and big % i == 0:
            result = i * (small//i) * (big//i)
            break
    if result == 0:
        result = small * big
    
    print(result)

# 함수 이용
def LCM(a, b):
    d = GCD(a, b)
    return int((a * b) / d)
def GCD(a, b):
    return GCD(b%a, a) if b%a else a
    
T = int(input())
for _ in range(T):
    a, b  = map(int, input().split())
    print(LCM(a, b))