'''
14716. 현수막

ANT가 처음 알고리즘 대회를 개최하게 되면서 현수막을 내걸었다.
저번 학기 영상처리 수업을 듣고 배웠던 지식을 최대한 응용 해보고 싶은 혁진이는이 현수막에서 글자가 몇 개인지 알아보는 프로그램을 만들려 한다.
혁진이는 우선 현수막에서 글자인 부분은 1, 글자가 아닌 부분은 0으로 바꾸는 필터를 적용하여 값을 만드는데 성공했다.
그런데 혁진이는 이 값을 바탕으로 글자인 부분 1이 상, 하, 좌, 우, 대각선으로 인접하여 서로 연결되어 있다면 한 개의 글자라고 생각만 하였다.
혁진이가 필터를 적용하여 만든 값이 입력으로 주어졌을 때, 혁진이의 생각대로 프로그램을 구현하면 글자의 개수가 몇 개인지 출력하여라.
'''
# 상하좌우, 대각선 델타값
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

def DFS(start_x, start_y):
    # 방문 표시
    visited[start_x][start_y] = 1
    stack = [(start_x, start_y)]
    while stack:
        x, y = stack.pop()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    if banner[nx][ny] == 1:
                        stack.append((nx, ny))

M, N = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(M)]

visited = [[0] * N for _ in range(M)]
char_cnt = 0

for i in range(M):
    for j in range(N):
        if banner[i][j] == 1 and not visited[i][j]:
            char_cnt += 1
            DFS(i, j)

print(char_cnt)

'''
[입력]
8 19
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 0
0 0 1 0 1 0 0 1 1 0 0 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0
0 1 1 1 1 1 0 1 0 1 0 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 0 1 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

[출력]
3
'''