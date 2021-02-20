'''
1100. 하얀 칸

체스판은 8*8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다.
가장 왼쪽 위칸 (0,0)은 하얀색이다. 
체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.
'''
# 8 X 8 체스판의 상태 입력
SIZE = 8
chess = [list(input()) for _ in range(SIZE)]
cnt = 0
for i in range(SIZE):
    for j in range(SIZE):
        # 짝수 줄에 있는 경우
        if i % 2 == 0 and j % 2 == 0:
            if chess[i][j] == 'F':
                cnt += 1
        # 홀수 줄에 있는 경우
        elif i % 2 and j % 2:
            if chess[i][j] == 'F':
                cnt += 1
print(cnt)
'''
[입력]
.F.F...F
F...F.F.
...F.F.F
F.F...F.
.F...F..
F...F.F.
.F.F.F.F
..FF..F.

[출력]
1
'''