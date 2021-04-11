'''
2178. 미로 탐색

N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(x, y):
    queue = [(x, y)]
    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0 and maze[nr][nc] == 1:            
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
BFS(0, 0)
print(visited[N-1][M-1])
'''
[입력]
4 6
101111
101010
101011
111011

[출력]
15
'''