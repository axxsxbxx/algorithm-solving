'''
1247. 부호

N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성하시오.
'''
# 시간 초과 코드
for _ in range(3):
    s = 0
    
    for n in range(int(input())):
        s += int(input())
    
    if s > 0:
        print('+')
    elif s < 0:
        print('-')
    else:
        print(0)


# stdin.readline 사용
from sys import stdin

for _ in range(3):
    N = int(stdin.readline())
    num = [int(stdin.readline()) for i in range(N)]
    
    if sum(num) > 0:
        print('+')
    elif sum(num) < 0:
        print('-')
    else:
        print(0)

'''
[입력]
3
0
0
0
10
1
2
4
8
16
32
64
128
256
-512
6
9223372036854775807
9223372036854775806
9223372036854775805
-9223372036854775807
-9223372036854775806
-9223372036854775804

[출력]
0
-
+
'''