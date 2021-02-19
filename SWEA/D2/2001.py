'''
2001. 파리 퇴치

N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.

M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!
'''
# M X M 파리채로 내리쳐서 죽인 파리 수의 합을 구하는 함수
def fly_sum(i, j, m, fly):
    m_sum = 0
    for x in range(m):
        for y in range(m):
            m_sum += fly[i+x][j+y]
    return m_sum

# 가장 많이 죽은 파리의 수를 구하는 함수
def get_max_fly(n, m, fly):
    max_fly = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            num = fly_sum(i, j, m, fly)
            if num > max_fly:
                max_fly = num
    return max_fly

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    # N X N 배열 생성
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = get_max_fly(N, M, arr)
    print('#%d %d' % (t, ans))

'''
[입력]
1
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

[출력]
#1 49
'''