'''
1945. 간단한 소인수분해

숫자 N은 아래와 같다.
N=2a x 3b x 5c x 7d x 11e
N이 주어질 때 a, b, c, d, e 를 출력하라.
'''
def get_result(num):
    cnt = [0] * 5
    base = [2, 3, 5, 7, 11]
    for i, n in enumerate(base):
        while num % n == 0 and num // n > 0:
            cnt[i] += 1
            num /= n
    return cnt

T = int(input())
for t in range(1, T+1):
    number = int(input())
    result = ' '.join(map(str, get_result(number)))
    print('#%d %s' % (t, result))
'''
[입력]
10  
6791400
1646400
1425600
8575
185625
6480
1185408
6561
25
330750

[출력]
#1 3 2 2 3 1
#2 6 1 2 3 0
#3 6 4 2 0 1
#4 0 0 2 3 0
#5 0 3 4 0 1
#6 4 4 1 0 0
#7 7 3 0 3 0
#8 0 8 0 0 0
#9 0 0 2 0 0
#10 1 3 3 2 0
'''