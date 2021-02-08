'''
1966. 숫자를 정렬하자

주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
'''
def number_sort(N, l):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


T = int(input())
for t in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split()))
    result = number_sort(N, D)
    ans = ' '.join(list(map(str, result)))
    print('#%d %s' % (t, ans))

'''
[입력]
1
5
1 4 7 8 0

[출력]
#1 0 1 4 7 8
'''