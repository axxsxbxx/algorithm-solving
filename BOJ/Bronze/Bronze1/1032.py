'''
1032. 명령 프롬프트

검색 결과가 먼저 주어졌을 때, 패턴으로 뭘 쳐야 그 결과가 나오는지를 출력하는 문제이다. 
패턴에는 알파벳과 "." 그리고 "?"만 넣을 수 있다. 가능하면 ?을 적게 써야 한다. 
그 디렉토리에는 검색 결과에 나온 파일만 있다고 가정하고, 파일 이름의 길이는 모두 같다.
'''
# 파일 이름의 개수 N
N = int(input())
# 파일 이름 저장
files = [list(input()) for _ in range(N)]
# 파일 이름의 길이는 모두 같음
length = len(files[0])
# 파일 이름들 중 다른 문자가 존재하는 위치 pos에 저장
pos = []
for i in range(length):
    for j in range(N-1):
        if files[j][i] != files[j+1][i]:
            pos.append(i)
            break
# pos에 저장되어 있는 위치에는 ?를, 아니면 원래 가지고 있던 문자를 저장
result = ''
for i in range(length):
    if i in pos:
        result += '?'
    else:
        result += files[0][i]
print(result)
'''
[입력]
3
config.sys
config.inf
configures

[출력]
config????
'''