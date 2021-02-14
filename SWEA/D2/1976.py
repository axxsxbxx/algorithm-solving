'''
1976. 시각 덧셈

시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.
(시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)
'''
# 테스트 케이스 개수
T = int(input())

for t in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    hour = h1 + h2
    minute = m1 + m2
    
    if minute > 59:
        hour += minute // 60
        minute %= 60

    if hour > 12:
        hour %= 12
        if hour == 0:
            hour = 12

    print('#{} {} {}'.format(t, hour, minute))

'''
[입력]
3
3 17 1 39
8 22 5 10
6 53 2 12

[출력]
#1 4 56
#2 1 32
#3 9 5
'''