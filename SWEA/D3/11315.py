'''
11315. 오목 판정

N X N 크기의 판이 있다. 판의 각 칸에는 돌이 있거나 없을 수 있다. 
돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.
각 테스트 케이스 마다 돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력한다.
'''
def chk(row, col):
    # 오목이 있으면 return 'YES'
    # 없으면 return 'NO'

    # 시작점 BRD[row][col] 가로
    # 델타 이용(가로, 세로, 왼쪽대각선, 오른쪽 대각선 순)
    dr = [0, 1, 1, 1] # x축
    dc = [1, 0, -1, 1] # y축

    for i in range(4):
        cnt = 0
        idxr = row
        idxc = col

        while 0 <= idxr < N and 0 <= idxc < N and BRD[idxr][idxc] == 'o':
            idxr += dr[i]
            idxc += dc[i]
            cnt += 1
            if cnt == 5:
                return 'YES'
    return 'NO'

T = int(input())
for t in range(1, T+1):
    N = int(input())
    BRD = [input() for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if BRD[r][c] == 'o':
                res = chk(r, c)
                if res == 'YES':
                    break
        if res == 'YES':
            break

    print('#%d %s' % (t, res))
'''
[입력]
2
5
....o
...o.
..o..
.o...
o....
5
...o.
ooooo
...o.
...o.
.....

[출력]
#1 YES
#2 YES
'''