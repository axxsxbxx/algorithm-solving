'''
1157. 단어 공부

알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.
'''
# 왜 틀렸다고 나오지...?
word = input()
word = word.upper()
alpha = set(word)
max_cnt = 0

for a in alpha:
    cnt = word.count(a)
    if cnt == max_cnt:
        max_alpha = '?'
        break
    if cnt > max_cnt:
        max_cnt = cnt
        max_alpha = a

print(max_alpha)

# 다른 방식
words = input().upper()
alpha = list(set(words)) 

cnt_list = []
for x in alpha :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(alpha[max_index])
'''
[입력]
Mississipi
zZa

[출력]
?
Z
'''