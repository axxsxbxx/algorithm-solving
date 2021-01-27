'''
2027. 대각선 출력하기
주어진 텍스트를 그대로 출력하세요.
'''

for i in range(5):
    result = ['+' for _ in range(5)]
    result[i] = '#'
    print(''.join(result))


'''
출력 : 
#++++
+#+++
++#++
+++#+
++++#
'''