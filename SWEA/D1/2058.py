'''
2058. 자릿수 더하기

하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
'''
# 첫 번째 방법
number = input()
sum = 0
for num in number:
    sum += int(num)
print(sum)

# 두 번째 방법
number = int(input())
sum = 0
while number > 0:
    sum += (number % 10)
    number //= 10
print(sum)
'''
[입력]
6789

[출력]
30
'''