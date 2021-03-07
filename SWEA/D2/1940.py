'''
1940. 가랏! RC카!
입력으로 매 초마다 아래와 같은 command 가 정수로 주어진다.

0 : 현재 속도 유지.
1 : 가속
2 : 감속

위 command 중, 가속(1) 또는 감속(2) 의 경우 가속도의 값이 추가로 주어진다.
가속도의 단위는, m/s**2 이며, 모두 양의 정수로 주어진다.
입력으로 주어진 N 개의 command 를 모두 수행했을 때, N 초 동안 이동한 거리를 계산하는 프로그램을 작성하라.
'''
T = int(input())
for t in range(1, T+1):
    N = int(input())
    speed = 0
    dist = 0
    for _ in range(N):
        command = list(map(int, input().split()))
        # 현재 속도 유지
        if command[0] == 0:
            dist += speed
        # 가속 하는 경우
        elif command[0] == 1:
            speed += command[1]
            dist += speed
        # 감속 하는 경우
        else:
            if command[1] > speed:
                speed = 0
            else:
                speed -= command[1]
                dist += speed
    print('#%d %d' % (t, dist))
'''
[입력]
3
2
1 2
2 1
3
1 1
0
1 1
5
1 2
1 2
2 1
0
0

[출력]
#1 3
#2 4
#3 15
'''