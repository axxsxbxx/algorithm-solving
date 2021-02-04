'''
1989. 초심자의 회문 검사

"level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.
'''
t = int(input())
test_case = []

for _ in range(t):
    # 테스트 케이스 입력값에 포함된 공백 삭제
    test_case.append(list(input().strip()))

# reversed 이용
for i, word in enumerate(test_case, start=1):
    reverse_word = list(reversed(word))
    # reversed한 단어와 같으면 1을, 다르면 0을 출력
    if word == reverse_word:
        result = 1
    else:
        result = 0

    print(f'#{i} {result}')


'''
[입력]
3
level     
samsung
eye    

[출력]
#1 1
#2 0
#3 1
'''