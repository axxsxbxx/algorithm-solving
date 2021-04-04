'''
3699. 주차빌딩

주차 빌딩의 원리는 간단하다. 차를 주차 타워의 입구에 있는 엘리베이터에 주차시키고 차에서 내린다. 
엘리베이터와 컨베이어 벨트는 빈 주차 공간을 찾아 그곳으로 이동시킨다. 차를 찾으러 오기 전까지 차는 계속 그곳에 있는다. 
차를 찾으러 오면, 엘리베이터와 컨베이어 벨트는 해당하는 차를 찾아 다시 입구로 가져온다.

주차 빌딩의 레이아웃은 간단하다. 빌딩에는 중앙 엘리베이터가 있고, 차는 엘리베이터를 이용해서 층 사이를 이동할 수 있다. 
각 층에는 거대한 원형 컨베이어 벨트가 있으며, 이 컨베이어 벨트 위에 차가 있다. 벨트는 시계방향, 반시계방향으로 움직일 수 있다. 
엘리베이터가 어떤 층에 도착했을 때, 컨베이어 벨트의 일부가 되며, 차는 엘리베이터를 통과해서 이동할 수 있다.

하루 일과가 끝날 때 쯤이면, 많은 사람들이 차를 다시 찾으러 주차 빌딩으로 온다. 
사람들은 온 순서대로 차를 찾을 수 있다. 엘리베이터는 차가 있는 곳으로 이동하고, 컨베이어 벨트는 차를 엘리베이터에 싣고, 다시 아래로 내려가 고객에게 차를 전달해준다. 
모든 손님이 차를 찾는데 걸리는 시간을 구하는 프로그램을 작성하시오. 
엘리베이터가 층을 이동하는데 걸리는 시간은 10초이고, 컨베이어 벨트가 차 한 대 만큼 시게방향 또는 반시계방향으로 이동하는데 걸리는 시간은 5초이다. 
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h, l = map(int, input().split())
    building = [list(map(int, input().split())) for _ in range(h)]
    
    cars = []
    # level은 층 수, pos는 위치
    for level in range(h):
        for pos in range(l):
            if building[level][pos] != -1:
                cars.append([level, pos, building[level][pos]])
    # 손님이 줄 서 있는 순서대로 정렬
    cars.sort(key = lambda x:x[2])
    # print(cars)
    time = 0
    # 각 층에 있는 엘레베이터 위치에 존재하는 컨베이어 벨트 위치 저장하는 배열
    now_pos = [0] * h    
    for car in cars:
        level = car[0]
        # 찾아야하는 차의 위치(컨베이어 벨트 상에서)
        pos = car[1]
        # 층을 이동하는 시간 계산(올라갔다가 내려가는 시간 둘 다 계산해야해서 2를 곱한다.)
        time += 10 * 2 * level
        # 현재 위치와 찾아야 하는 자동차의 위치 사이의 거리
        dist = abs(now_pos[level] - pos)
        # 컨베이어 벨트이기 때문에 시계 방향과 반시계 방향 중 더 적은 거리를 선택한다.
        time += 5 * min(dist, l - dist)
        # 현재 층의 컨베이어 벨트 위치를 저장한다.
        now_pos[level] = pos
    
    print(time)
'''
[입력]
2
1 5
-1 2 1 -1 3
3 6
-1 5 6 -1 -1 3
-1 -1 7 -1 2 9
-1 10 4 1 8 -1

[출력]
25
320
'''