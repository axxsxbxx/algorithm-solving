'''
3052. 나머지

두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 
예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다. 
수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
'''
numbers = []
for _ in range(10):
    n = int(input())
    numbers.append(n)
cnt = [0] * 42
for num in numbers:
    cal = num % 42
    cnt[cal] = 1
print(cnt.count(1))
'''
[입력]
1
2
3
4
5
6
7
8
9
10
[출력]
10
'''