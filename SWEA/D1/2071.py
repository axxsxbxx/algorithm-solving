'''
2071. 평균값 구하기

10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
(소수점 첫째 자리에서 반올림한 정수를 출력한다.)
'''
t = int(input())
test_case = []

for _ in range(t):
    test_case.append(input().split())

for i, numbers in enumerate(test_case, start=1):
    sum = 0
    for num in numbers:
         sum += int(num)
    print(f'#{i} {round(sum/len(numbers))}')

'''
[입력]
3
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1

[출력]
#1 24
#2 29
#3 27
'''