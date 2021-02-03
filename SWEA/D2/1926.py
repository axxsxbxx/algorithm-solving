'''
1926. 간단한 369 게임

입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를
게임 규칙에 맞게 출력하는 프로그램을 작성하라.
박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.
여기서 주의해야 할 것은 박수 한 번 칠 때는 - 이며, 박수를 두 번 칠 때는 - - 가 아닌 -- 이다. 
'''
N = int(input())
result = []
# 1부터 N까지
for n in range(1, N+1):
    # 3, 6, 9의 개수를 셀 변수 초기화
    cnt = 0
    # n을 문자열으로 변경함
    num = str(n)
    # 각 자리마다 3, 6, 9가 있으면 cnt 증가
    for a in num:
        if a in ('3', '6', '9'):
            cnt += 1
    # 결과적으로 3, 6, 9의 개수가 0이면 원래 숫자 추가
    if cnt == 0:
        result.append(n)
    # 아니면 3, 6, 9의 개수만큼 - 추가
    else:
        result.append('-' * cnt)

print(*result)

'''
[입력]
10

[출력]
1 2 - 4 5 - 7 8 - 10
'''