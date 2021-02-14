'''
4344. 평균은 넘겠지

대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다.
당신은 그들에게 슬픈 진실을 알려줘야 한다.
'''
# 테스트 케이스 수 
c = int(input())

for _ in range(c):
    numbers = list(map(int, input().split()))
    # 학생의 수
    n = numbers[0]
    # n명의 점수
    scores = numbers[1:]
    # 평균 구하기
    avg = sum(scores) / n
    # 평균 넘는 학생 수 카운트
    cnt = 0
    # 평균 넘는 학생 수 구하기
    for score in scores:
        if score > avg:
            cnt += 1
    # 평균을 넘는 학생들의 비율 구하기
    per = cnt / n * 100
    print('{0:.3f}%'.format(per))
'''
[입력]
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91

[출력]
40.000%
57.143%
33.333%
66.667%
55.556%
'''