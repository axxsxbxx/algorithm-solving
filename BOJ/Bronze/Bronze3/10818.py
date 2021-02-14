'''
10818. 최소, 최대

N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
'''
# max, min 사용
n = int(input())
numbers = list(map(int, input().split()))
print('{} {}'.format(min(numbers), max(numbers)))

# max, min 사용 X
n = int(input())
numbers = list(map(int, input().split()))
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print('{} {}'.format(min_num, max_num))
'''
[입력]
5
20 10 35 30 7

[출력]
7 35
'''