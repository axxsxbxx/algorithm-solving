'''
2019. 더블더블

1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
주어질 숫자는 30을 넘지 않는다.
'''
n = int(input())
result = []

for i in range(n+1):
    if i == 0:
        result.append(1)
        num = 1
    else:
        result.append(num * 2)
        num *= 2

print(*result)
     
'''
입력 : 8
출력 : 1 2 4 8 16 32 64 128 256
'''