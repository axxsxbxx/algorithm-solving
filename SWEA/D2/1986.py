'''
1986. 지그재그 숫자

1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

N이 5일 경우,
1 – 2 + 3 – 4 + 5 = 3
N이 6일 경우,
1 – 2 + 3 – 4 + 5 – 6 = -3
'''
# 테스트 케이스
t = int(input())
test_case = []

for _ in range(t):
    test_case.append(int(input()))

for i, num in enumerate(test_case, start=1):

    for n in range(1, num+1):
        
    
    print(f'#{i} {}')
'''
[입력]
2
5
6

[출력]
#1 3
#2 -3
'''