'''
1204. 최빈수 구하기

어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.
이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.
다음과 같은 수 분포가 있으면,
10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
최빈수는 8이 된다.
최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).
'''
# 테스트 케이스 수
t = int(input())
test_case = []
# 테스트 케이스 입력 받음
for _ in range(t):
    input()
    test_case.append(input())
# 테스트 케이스 하나씩 검사
for i, test in enumerate(test_case, start=1):
    # 문자열로 받은 숫자들 int로 변환 후 리스트로 저장
    test_num = list(map(int, test.split()))
    # test_num에 있는 숫자들 중복 제거함
    unique_num = set(test_num)
    # test_num의 첫번째 수를 result로 저장
    result = test_num[0]
    # 유일한 숫자 하나씩 꺼내서
    for num in unique_num:
        # 하나씩 count 이용해서 숫자 비교함
        if test_num.count(num) > test_num.count(result):
            result = num
        # 가지고 있는 개수가 똑같으면 더 큰 수를 저장함
        elif test_num.count(num) == test_num.count(result):
            if num > result:
                result = num

    print(f'#{i} {result}')

'''
[입력]
1
1
10 8 7 2 2 4 8 8 8 9 5 5 3

[출력]
#1 8
'''
