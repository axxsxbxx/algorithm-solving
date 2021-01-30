'''
2070. 큰 놈, 작은 놈, 같은 놈

2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.
'''
t = int(input())
test_case = []
for _ in range(t):
    test_case.append(input().split())

for i, test in enumerate(test_case, start=1):
    a , b = test
    a = int(a)
    b = int(b)

    if a > b:
        result = '>'
    elif a < b:
        result = '<'
    else:
        result = '='

    print(f'#{i} {result}')

'''
[입력]
3
3 8 
7 7 
369 123      

[출력]
#1 <
#2 =
#3 >
'''