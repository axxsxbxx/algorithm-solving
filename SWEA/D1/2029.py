'''
2029. 몫과 나머지 출력하기
2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.
'''
t = int(input())
test_case = []

for _ in range(t):
    a = input().split()
    test_case.append(a)

for num in range(t):
    a, b = divmod(int(test_case[num][0]), int(test_case[num][1]))
    print(f'#{num + 1} {a} {b}')

'''
[입력] 
3   
9 2  
15 6 
369 15

[출력]
#1 4 1
#2 2 3
#3 24 9
'''