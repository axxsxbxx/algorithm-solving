'''
2005. 파스칼의 삼각형

크기가 N인 파스칼의 삼각형을 만들어야 한다.
파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.
'''
T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 파스칼 삼각형 전체 구조 만들기
    tri = [['']*i for i in range(1, N+1)]
    for i in range(N):
        for j in range(i+1):
            # 첫째열에 존재하는 건 모두 1
            if j == 0:
                tri[i][j] = 1
            # 각 행에서 마지막에 해당하는 건 모두 1
            elif j == i:
                tri[i][j] = 1
            # 나머지는 위의 두개 숫자 더한 값
            else:
                tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
    print('#%d' % t)
    for num in tri:
        print(' '.join(map(str, num)))

'''
[입력]
1
4

[출력]
#1
1
1 1
1 2 1
1 3 3 1
'''
