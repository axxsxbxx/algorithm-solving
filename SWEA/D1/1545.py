'''
1545. 거꾸로 출력해보아요
주어진 숫자부터 0까지 순서대로 찍어보세요.
'''
num = int(input())

for i in range(num, -1, -1):
    print(i, end=' ')