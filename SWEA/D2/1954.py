'''
1954. 달팽이 숫자

달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오
'''
def get_snail_num(n):
    # 우하좌상 순으로 규칙적으로 진행됨
    # 이에 따른 델타 좌표 dx, dy
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # 달팽이 숫자 저장할 리스트
    snail = [[0] * n for _ in range(n)]
    num = 1
    # 델타 좌표 활용하기 위한 변수 base
    base = 0
    x, y = 0, -1
    # n이 3일 때 3 2 2 1 1 이런식으로 진행
    # 첫 번째 경우만 따로 처리
    for _ in range(n):
        x += dx[base]
        y += dy[base]
        snail[x][y] = num
        num += 1
    # 반복되는 경우 처리
    for i in range(n-1, 0, -1):
        for _ in range(2):
            base += 1
            for _ in range(i):
                x += dx[base%4]
                y += dy[base%4]
                snail[x][y] = num
                num += 1
    return snail

T = int(input())
for t in range(1, T+1):
    number = int(input())
    print('#%d' % t)
    result = get_snail_num(number)
    for line in result:
        print(*line)
'''
[입력]
2    
3   
4 

[출력]
#1
1 2 3
8 9 4
7 6 5
#2
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
'''