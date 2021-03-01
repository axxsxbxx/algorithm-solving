'''
1860.
진기는 붕어빵 가게를 운영하고 있다.
진기가 파는 붕어빵은 그냥 붕어빵이 아니라 겉은 바삭! 속은 말랑! 한입 물면 팥 앙금이 주르륵 흘러 입안에서 춤을 추며,
절로 어릴 적 호호 불며 먹었던 뜨거운 붕어빵의 추억이 떠올라 눈물이 나오게 되는 최고급 붕어빵이다.
진기는 이런 붕어빵을 보통 사람들에게는 팔지 않는다.
그는 무조건 예약제로만 손님을 받으며, 예약을 하려는 손님들은 진기의 까다로운 자격 검증에서 합격해야만 붕어빵을 맛 볼 자격을 얻는다.
그래서 오늘은 N명의 사람이 자격을 얻었다.
진기는 0초부터 붕어빵을 만들기 시작하며, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.
서빙은 진기가 하는 것이 아니기 때문에, 붕어빵이 완성되면 어떤 시간 지연도 없이 다음 붕어빵 만들기를 시작할 수 있다.
0초 이후에 손님들이 언제 도착하는지 주어지면, 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하는 프로그램을 작성하라.
'''
def get_result(customer, n, m, k):
    arrive = sorted(customer)
    for i in range(n):
        if (arrive[i] // m) * k < i + 1:
            return 'Impossible'
    return 'Possible'


T = int(input())
for t in range(1, T+1):
    # N명의 손님이 오고, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.
    N, M, K = map(int, input().split())
    second = list(map(int, input().split()))
    ans = get_result(second, N, M, K)
    print('#%d %s' % (t, ans))
'''
[입력]
4
2 2 2
3 4
2 2 2
1 2
2 2 1
4 2
2 2 1
3 2

[출력]
#1 Possible
#2 Impossible
#3 Possible
#4 Impossible
'''