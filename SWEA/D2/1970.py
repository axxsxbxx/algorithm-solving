'''
1970. 쉬운 거스름돈
우리나라 화폐 ‘원’은 금액이 높은 돈을 우선적으로 계산할 때 돈의 개수가 가장 최소가 된다.

S마켓에서 사용하는 돈의 종류는 다음과 같다.
50,000 원
10,000 원
5,000 원
1,000 원
500 원
100 원
50 원
10 원

S마켓에서 손님에게 거슬러 주어야 할 금액 N이 입력되면 돈의 최소 개수로 거슬러 주기 위하여 각 종류의 돈이 몇 개씩 필요한지 출력하라.
'''
def change(money):
    result = [0] * 8
    base = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i, n in enumerate(base):
        while money >= n:
            money -= n
            result[i] += 1
    return result


T = int(input())
for t in range(1, T+1):
    N = int(input())
    ans = ' '.join(list(map(str, change(N))))
    print('#%d' % t)
    print('%s' % ans)
            

'''
[입력]
2
32850
160

[출력]
#1
0 3 0 2 1 3 1 0
#2
0 0 0 0 0 1 1 1
'''