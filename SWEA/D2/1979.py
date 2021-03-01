'''
1979. 어디에 단어가 들어갈 수 있을까

N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.
'''
# 열 검사 부분에서 문제 발생
# T = int(input())
# for t in range(1, T+1):
#     N, K = map(int, input().split())
#     my_puzzle = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0

#     for i in range(N):
#         cnt = 0
#         # 행을 검사
#         for j in range(N):
#             if my_puzzle[i][j] == 1:
#                 cnt += 1
#             # 해당 칸이 0이거나 마지막의 전 칸 일때
#             if my_puzzle[i][j] == 0 or j == N-1:
#                 # cnt가 K와 같다면
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#         # 열을 검사
#         for j in range(N):
#             if my_puzzle[j][i] == 1:
#                 cnt += 1
#             if my_puzzle[j][i] == 0 or i == N-1:
#                 if cnt == K:
#                     ans += 1
#                 cnt = 0
#     print('#%d %d' % (t, ans))

def get_result(puzzle, n, k):
    ans = 0
    for i in range(n):
        cnt = 0
        # 행을 검사
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == n - 1:
                if cnt == k:
                    ans += 1
                cnt = 0
    return ans

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    my_puzzle = [list(map(int, input().split())) for _ in range(N)]
    puzzle_reverse = list(map(list, zip(*my_puzzle)))
    ans = get_result(my_puzzle, N, K) + get_result(puzzle_reverse, N, K)
    print('#%d %d' % (t, ans))
'''
[입력]
1
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1

[출력]
#1 2
'''