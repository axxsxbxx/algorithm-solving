'''
1959. 두 개의 숫자열

서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.
'''
def get_result(a, b):
    # a가 짧은 리스트, b가 긴 리스트
    n = len(a)
    m = len(b)
    max_num = -999999
    for i in range(m-n+1):
        sum = 0
        for j in range(n):
            sum += a[j] * b[i+j]
        if sum > max_num:
            max_num = sum
    return max_num


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        long = A
        short = B
    else:
        long = B
        short = A

    result = get_result(short, long)
    print('#%d %d' % (t, result))
'''
[입력]
2
3 5
1 5 3
3 6 -7 5 4
7 6
6 0 5 5 -1 1 6
-4 1 8 7 -9 3

[출력]
#1 30
#2 63
'''