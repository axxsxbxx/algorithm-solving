'''
1859. 백만 장자 프로젝트

25년 간의 수행 끝에 원재는 미래를 보는 능력을 갖게 되었다. 이 능력으로 원재는 사재기를 하려고 한다.
다만 당국의 감시가 심해 한 번에 많은 양을 사재기 할 수 없다.
다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.

    1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
    3. 판매는 얼마든지 할 수 있다.

예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.
'''
# 런타임 에러
# def max_profit(price):
#     # 팔아서 얻은 이익
#     profit = 0
#     while len(price) > 1:
#         max_price = max(price)
#         # 매매횟수
#         cnt = 0
#         # 구입에 든 비용
#         cost = 0
#         max_idx = 0
#         for i in range(len(price)):
#             if price[i] == max(price):
#                 max_idx = i
#                 break
#             cnt += 1
#             cost += price[i]
#         profit += (cnt * max_price - cost)
#         if len(price) == 2 and price[-1] == max_price:
#             break
#         price = price[max_idx+1:]
#
#     return profit

# 뒤에서부터 접근
def max_profit(price):
    max_price = price[-1]
    profit = 0
    for i in range(N - 1, -1, -1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            profit += max_price - price[i]
    return profit

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = max_profit(arr)
    print('#%d %d' % (t, ans))
'''
[입력]
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2

[출력]
#1 0
#2 10
#3 5
'''