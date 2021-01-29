'''
2068. 최대수 구하기

10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
'''
# 첫 번째 : max 이용
t = int(input())
test_case = []

for _ in range(t):
    test_case.append(input())

i = 1
for numbers in test_case:
    number_list = numbers.split()
    number = []
    for n in number_list:
        number.append(int(n))

    print(f'#{i} {max(number)}')
    i += 1

# 두 번째 : 비교하면서 찾아가기
t = int(input())
test_case = []

for _ in range(t):
    test_case.append(input())

i = 1
for numbers in test_case:
    number_list = numbers.split()
    number = []
    for n in number_list:
        number.append(int(n))    
    
    max_num = number[0]
    for n in number:
        if n > max_num:
            max_num = n

    print(f'#{i} {max_num}')
    i += 1



'''
[입력]
3 
3 17 1 39 8 41 2 32 99 2
22 8 5 123 7 2 63 7 3 46
6 63 2 3 58 76 21 33 8 1   

[출력]
#1 99
#2 123
#3 76
'''