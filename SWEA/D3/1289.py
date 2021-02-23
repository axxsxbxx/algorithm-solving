'''
1289.원재의 메모리 복구하기

원재가 컴퓨터를 만지다가 실수를 저지르고 말았다. 메모리가 초기화된 것이다.
다행히 원래 메모리가 무슨 값이었는지 알고 있었던 원재는 바로 원래 값으로 되돌리려고 했으나 메모리 값을 바꿀 때 또 문제가 생겼다.
메모리 bit중 하나를 골라 0인지 1인지 결정하면 해당 값이 메모리의 끝까지 덮어씌우는 것이다.
예를 들어 지금 메모리 값이 0100이고, 3번째 bit를 골라 1로 설정하면 0111이 된다.
원래 상태가 주어질 때 초기화 상태 (모든 bit가 0) 에서 원래 상태로 돌아가는데 최소 몇 번이나 고쳐야 하는지 계산해보자.
'''
def get_result(num):
    length = len(num)
    # 초기값
    base = ['0'] * length
    # 최소 수정횟수
    cnt = 0
    while True:
        # base와 num이 같아질 때 최소 수정횟수 반환
        if base == num:
            return cnt
        for i in range(length):
            # 초기값과 원래 값이 다른 지점이 있으면
            if base[i] != num[i]:
                # 수정횟수 1회 증가
                cnt += 1
                # i부터 끝까지 num[i]에 있는 값으로 변경
                for j in range(i, length):
                    base[j] = num[i]

def get_count(num):
    # 다른 방법(0-1로 바뀌는 곳의 count만 세는것)
    cnt = 0
    if num[0] == '1':
        cnt = 1
    for i in range(len(num) - 1):
        if num[i] != num[i + 1]:
            cnt += 1
    return cnt

T = int(input())
for t in range(1, T+1):
    # 원래 상태
    origin = list(input())
    ans = get_result(origin)
    print('#%d %d' % (t, ans))
'''
[입력]
2
0011
100

[출력]
#1 1
#2 2
'''