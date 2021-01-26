'''
1933. 간단한 N의 약수
입력으로 1개의 정수 N 이 주어진다.
정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
'''
num = int(input())

result = []
for i in range(1, num+1):
    if num % i == 0:
        result.append(i)

print(*result)

'''
입력 : 10
출력 : 1 2 5 10
'''