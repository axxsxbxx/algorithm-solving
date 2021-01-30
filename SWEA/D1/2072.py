'''
2075. 홀수만 더하기

10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
'''
t = int(input())
test_case = []

for _ in range(t):
    test_case.append(input().split())

for i, numbers in enumerate(test_case, start=1):
    sum = 0
    for num in numbers:
        n = int(num)
        if n % 2:
            sum += n
    print(f'#{i} {sum}')


'''
[입력]
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   

[출력]
#1 200
#2 208
#3 121
'''