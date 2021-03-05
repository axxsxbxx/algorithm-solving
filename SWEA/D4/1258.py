'''
1258. 행렬찾기

유엔 조사단은 화학 물질이 담긴 용기들로부터 3가지 사항을 발견하였다.

1. 화학 물질이 담긴 용기들이 사각형을 이루고 있다. 또한, 사각형 내부에는 빈 용기가 없다.
2. 화학 물질이 담긴 용기들로 이루어진 사각형들은 각각 차원(가로의 용기 수 x 세로의 용기 수)이 다르다.
3. 2개의 화학 물질이 담긴 용기들로 이루어진 사각형들 사이에는 빈 용기들이 있다.

유엔 조사단은 창고의 용기들에 대한 2차원 배열에서 행렬(화학 물질이 든 용기들로 이루어진 사각형)들을 찾아내고 정보를 수집하고자 한다.
찾아낸 행렬들의 정보를 출력하는 프로그램을 작성하시오.

각 줄은 ‘#x’로 시작하고 공백을 하나 둔 다음, 각 테스트 케이스에 주어진 행렬에서 추출된 부분 행렬들을 개수와 그 뒤를 이어 행렬들의 행과 열의 크기를 출력한다.
크기는 행과 열을 곱한 값으로, 크기가 작은 순서대로 출력한다.
예를 들어 3x4 행렬의 크기는 3*4 = 12 이다.
크기가 같을 경우 행이 작은 순으로 출력한다.
예를 들어 12x4, 8x6 두 개의 행렬은 같은 크기이고 행은 각각 12, 8 이므로 8 6 12 4 순으로 출력한다.
'''
# 반복문
# 상좌 델타값
dx = [-1, 0]
dy = [0, -1]

def get_start(arr):
    starts = []
    for x in range(size):
        for y in range(size):
            # (x,y)가 0이 아니고
            if arr[x][y]:
                # 우측과 좌측이 0이면 starts에 값 추가
                base = []
                for i in range(2):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    base.append(arr[nx][ny])
                if sum(base) == 0:
                    starts.append((x, y))
    return starts

def get_rc(starts, arr):
    result = []
    for sx, sy in starts:
        # 행의 크기 구하기
        row_cnt = 0
        for i in range(sx, size):
            if arr[i][sy] == 0:
                break
            row_cnt += 1

        # 열의 크기 구하기
        col_cnt = 0
        for i in range(sy, size):
            if arr[sx][i] == 0:
                break
            col_cnt += 1

        result.append((row_cnt, col_cnt))
    return result


T = int(input())
for t in range(1, T+1):
    n = int(input())
    container = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
    container.insert(0, [0]*(n+2))
    container.append([0] * (n+2))
    size = n + 2
    start_point = get_start(container)
    ans = get_rc(start_point, container)
    ans.sort(key=lambda x: (x[0] * x[1], x[0]))
    print('#%d %d' % (t, len(ans)), end=' ')
    for x, y in ans:
        print('%d %d' % (x, y), end=' ')
    print()

'''
[입력]
1
9
1 1 3 2 0 0 0 0 0
3 2 5 2 0 0 0 0 0
2 3 3 1 0 0 0 0 0
0 0 0 0 4 5 5 3 1
1 2 5 0 3 6 4 2 1
2 3 6 0 2 1 1 4 2
0 0 0 0 4 2 3 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

[출력]
#1 3 2 3 3 4 4 5
'''