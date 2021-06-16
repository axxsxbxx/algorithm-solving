'''
1248. 맞춰봐

https://www.acmicpc.net/problem/1248
'''
# 체크 필요한 경우
def check(idx):
    s = 0
    # i부터 i번째까지, i-1부터 i번째까지 .... 0부터 i번째까지(열의 아래에서 위로 더해간다)
    # 그러면 제일 먼저 실시하는 검사가 무조건 i에서 i까지의 합 --> i번째 수의 부호를 바로 알 수 있음
    for i in range(idx, -1, -1):
        s += ans[i]
        if s == 0 and S[i][idx] != '0':
            return False
        if s > 0 and S[i][idx] != '+':
            return False
        if s < 0 and S[i][idx] != '-':
            return False
    return True


def get_ans(idx):
    if idx == N:
        return True
    
    # 대각선에 있는게 0이면 해당 숫자도 0
    if S[idx][idx] == '0':
        ans[idx] = 0
        return get_ans(idx+1)

    for i in range(1, 11):
        ans[idx] = S[idx][idx] * i
        if check(idx) and get_ans(idx+1):
            return True
            
    return False

N = int(input())
sign = list(input())

# 행렬로 표현하기
S = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        temp = sign.pop(0)
        if temp == '+':
            sign[i][j] = 1
        elif temp == '-':
            sign[i][j] = -1

ans = [0] * N
get_ans(0)
print(*ans)

'''
[입력]
4
-+0++++--+

[출력]
-2 5 -3 1
'''