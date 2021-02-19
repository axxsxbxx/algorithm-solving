'''
1210. Ladder1
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 
사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.
김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.
사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 
좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.
방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 
지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라 
(‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다. 도착 지점은 '2'로 표현된다).
'''
def get_result(a):
    # 마지막 행에서 값이 2인 곳의 x, y 좌표 구하기
    for i in range(N):
        if a[N-1][i] == 2:
            y = i
            break
    x = N - 1
    # 첫번째 행에 도착할때까지 반복
    while x > 0:
        # 왼쪽으로 가는 경우
        if y > 0 and a[x][y-1] == 1:
            # y좌표가 0보다 크고 값이 0이 아닐때까지 반복
            while y > 0 and a[x][y-1] != 0:
                y -= 1
        # 오른쪽으로 가는 경우
        elif y < N-1 and a[x][y+1] == 1:
            # y좌표가 N-1 보다 작고 값이 0이 아닐때까지 반복
            while y < N-1 and a[x][y+1] != 0:
                y += 1
        # 위쪽으로 가는 경우
        x -= 1
    return y

N = 100
for _ in range(1, 11):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(N)]
    ans = get_result(ladder)
    print('#%d %d' % (t, ans))
'''
[입력]
1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 1 1 1
1 0 0 0 1 0 1 0 0 1
1 1 1 1 1 0 1 0 0 1
1 0 0 0 1 1 1 0 0 1
1 0 0 0 1 0 1 0 0 2

[출력]
#1 4
'''