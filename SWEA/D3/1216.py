'''
1216. 회문2

주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제이다.

각 칸의 들어가는 글자는 c언어 char type으로 주어지며 'A', 'B', 'C' 중 하나이다.
글자 판은 무조건 정사각형으로 주어진다.
ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다.
'''
def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-1-i]:
            return False
    return True

def max_palindrome(words):
    max_len = 0
    for word in words:
        for i in range(SIZE):
            for j in range(1, SIZE-i+1):
                if j > max_len:
                    if is_palindrome(word[i:i+j]):
                        max_len = j
    return max_len

SIZE = 100
for _ in range(10):
    t = input()
    my_string = [list(input()) for _ in range(SIZE)]
    # 세로로 회문 찾을 때 사용할 리스트
    my_string2 = list(zip(*my_string))
    ans = max(max_palindrome(my_string), max_palindrome(my_string2))
    print('#%s %d' % (t, ans))