'''
1206. View

강변에 빌딩들이 옆으로 빽빽하게 밀집한 지역이 있다.
이곳에서는 빌딩들이 너무 좌우로 밀집하여, 강에 대한 조망은 모든 세대에서 좋지만 왼쪽 또는 오른쪽 창문을 열었을 때 바로 앞에 옆 건물이 보이는 경우가 허다하였다.
그래서 이 지역에서는 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.
'''
# 해당 숫자와 앞뒤로 각각 2개씩 총 5개를 비교한다
# 5개 중 해당 숫자가 가장 큰 경우에만 조망권이 보장된다.
# 조망권이 보장되는 경우, 앞뒤로 각각 2개씩 총 4개의 숫자 중, 최대값과의 차만큼 보장된다.
def view(num, l):
    result = 0
    for i in range(2, num-2):
        max_num = l[i-2]
        # 앞뒤로 각각 2개씩 비교하기 위한 for문
        for j in [-2, -1, 1, 2]:
            if l[i+j] > l[i]:
                # 초기화를 0으로 하면 0 0 6 0 0과 같은 경우를 포함할 수 없음
                max_num = -1
                break
            # 앞뒤로 각각 2개씩, 4개의 숫자 중 최대값을 구한다.
            if l[i+j] >= max_num:
                max_num = l[i+j]
        # 5개 중 해당 숫자가 가장 큰 경우, 해당 숫자와 최대값의 차만큼 보장되는 조망권을 더한다.
        if max_num > -1:
            result += (l[i] - max_num)
    return result


def view2(num, l):
    result = 0
    for i in range(2, num-2):
        base = l[i]
        max_num = 0
        for j in [-2, -1, 1, 2]:
            if l[i+j] > max_num:
                max_num = l[i+j]
        if base > max_num:
            result += (base - max_num)
    return result


T = 10
for t in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split()))
    # ans = view(N, D)
    ans = view2(N, D)
    print('#%d %d' % (t, ans))

'''
[입력]
14
0 0 3 5 2 4 9 0 6 4 0 6 0 0

[출력]
6
'''