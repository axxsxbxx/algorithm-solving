'''
1938. 아주 간단한 계산기

1. 두 개의 자연수 a, b는 1부터 9까지의 자연수이다. (1 ≤ a, b ≤ 9)
2. 사칙연산 + , - , * , / 순서로 연산한 결과를 출력한다.
3. 나누기 연산의 결과에서 소수점 이하의 숫자는 버린다.
'''
# # map 쓰기 전 풀이
# a, b = input().split()
# a = int(a)
# b = int(b)

# map 사용
a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)


'''
입력 : 8 3
출력 : 
11
5
24
2
'''