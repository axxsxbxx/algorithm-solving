'''
1226. 미로1

아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.
주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.

테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).
'''
## 재귀 이용
# 상하좌우 델타값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_start(arr, n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '2':
                return i, j

def get_result(sx, sy):
    visited[sx][sy] = 1
    # 종료 조건
    if maze[sx][sy] == '3':
        global ans
        ans = 1
        return
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if 0 <= nx < SIZE and 0 <= ny < SIZE:
            if maze[nx][ny] != '1' and visited[nx][ny] == 0:
                get_result(nx, ny)

SIZE = 16
for _ in range(10):
    t = int(input())
    maze = [list(input()) for _ in range(SIZE)]
    start_x, start_y = get_start(maze, SIZE)
    visited = [[0]*SIZE for _ in range(SIZE)]
    ans = 0
    get_result(start_x, start_y)
    print('#%d %d' % (t, ans))

## 큐 이용
# 상하좌우 델타값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_start(arr, n):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return i, j

def get_result(sx, sy):
    queue = [(sx, sy)]
    visited = [[0] * SIZE for _ in range(SIZE)]
    visited[sx][sy] = 0
    while queue:
        target_x, target_y = queue.pop(0)
        for i in range(4):
            nx = target_x + dx[i]
            ny = target_y + dy[i]
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                if maze[nx][ny] == 3:
                    return 1
                if maze[nx][ny] != 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
    return 0

SIZE = 16
for _ in range(10):
    t = int(input())
    maze = [list(map(int, input())) for _ in range(SIZE)]
    start_x, start_y = get_start(maze, SIZE)
    ans = get_result(start_x, start_y)
    print('#%d %d' % (t, ans))