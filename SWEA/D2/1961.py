'''
1961. 숫자 배열 회전

N x N 행렬이 주어질 때,
시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.
'''
def turn_90(n, arr):
    new_arr = []
    for i in range(n):
        numbers = []
        for j in range(n-1, -1, -1):
            numbers += arr[j][i]
        new_arr.append(numbers)
    return new_arr


T = int(input())
for t in range(1, T+1):
    N = int(input())
    my_list = [list(input().split()) for _ in range(N)]

    list_90 = turn_90(N, my_list)
    list_180 = turn_90(N, list_90)
    list_270 = turn_90(N, list_180)

    print('#%d' % t)
    for i in range(N):
        print('%s %s %s' % (''.join(list_90[i]), ''.join(list_180[i]), ''.join(list_270[i])))
'''
[입력]
1
3
1 2 3
4 5 6
7 8 9

[출력]
#1
741 987 369
852 654 258
963 321 147
'''