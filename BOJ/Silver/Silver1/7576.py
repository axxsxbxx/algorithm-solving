'''
7576. 토마토

철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 
창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
'''
from collections import deque

N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(M)]

queue = deque()

for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            queue.append([i, j])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# bfs
while queue:
    r, c = queue.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N and box[nr][nc] == 0:
            box[nr][nc] = box[r][c] + 1
            queue.append([nr, nc])

result = -2
check = False
for i in box:
    for j in i:
        if not j:
            check = True
        result = max(result, j)

if check:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)



'''
[입력]
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

[출력]
8
'''