'''
4615. 재미있는 오셀로 게임
'''
T = int(input())
# 8방향 탐색을 위해 delta 선언
delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))

for t in range(1, T+1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    mid = n // 2

    board[mid][mid] = 2
    board[mid - 1][mid - 1] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1

    for i in range(m):
        x, y, c = map(int, input().split())
        y, x = y - 1, x - 1
        # 뒤집어야 할 돌을 저장할 리스트 reverse 초기화
        reverse = []
        # 8방향 탐색
        for i in range(8):
            dx, dy = delta[i]
            nx, ny = x + dx, y + dy
            while True:
                # 모서리인 경우
                if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
                    reverse = []
                    break
                # 빈 칸을 만난경우 reverse를 초기화
                if board[nx][ny] == 0:
                    reverse = []
                    break
                # 같은 색을 만났으므로 break
                if board[nx][ny] == c:
                    break
                # 조건에 부합하는 돌을 reverse에 추가한다.
                else:
                    reverse.append((nx, ny))
                nx, ny = nx + dx, ny + dy
            # 해당 돌의 색을 바꿔준다
            for rx, ry in reverse:
                if c == 1:
                    board[rx][ry] = 1
                else:
                    board[rx][ry] = 2
        board[x][y] = c
    # 각각의 돌 숫자를 세준다.
    black, white = 0, 0
    for i in range(n):
        black += board[i].count(1)
        white += board[i].count(2)

    print('#%d %d %d' % (t, black, white))