'''
2805. 농작물 수확하기

N X N크기의 농장이 있다. 이 농장에는 이상한 규칙이 있다.
규칙은 다음과 같다.
   ① 농장은 크기는 항상 홀수이다. (1 X 1, 3 X 3 … 49 X 49)
   ② 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.
농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.
'''
# 더해지는 수가 N=5일때 1행부터 1 3 5 3 1 순
def get_profit(farm, n):
    profit = 0
    base = n // 2
    check = 1
    for i in range(n):
        profit += (farm[i][base])
        if i <= base:
            # i=0 일때 X i=1 일때 1 i=2 일때 1 2
            for j in range(1, i+1):
                # 중점을 기준으로 양 옆 한칸씩 더함
                profit += farm[i][base-j]
                profit += farm[i][base+j]
        else:
            for j in range(i - 2*check, 0, -1):
                profit += farm[i][base - j]
                profit += farm[i][base + j]
            check += 1
    return profit

def get_profit2(farm, n):
    total = 0
    for i in range(n):
        start = n // 2
        end = n // 2
        for j in range(start, end):
            total += farm[i][j]

        if i > n//2:
            start += 1
            end -= 1
        else:
            start -= 1
            end += 1
    return total

T = int(input())
for t in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    ans = get_profit(farm, N)
    print('#%d %d' % (t, ans))
'''
[입력]
1
5
14054
44250
02032
51204
52212

[출력]
#1 23
'''