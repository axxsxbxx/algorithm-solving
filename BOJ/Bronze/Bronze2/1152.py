'''
1152. 단어의 개수

영어 대소문자와 띄어쓰기만으로 이루어진 문자열이 주어진다.
이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 
단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
'''
sentence = input().split()
print(len(sentence))
'''
[입력]
The Curious Case of Benjamin Button

[출력]
6
'''