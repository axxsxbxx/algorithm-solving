'''
1234. 비밀번호

평소에 잔머리가 발달하고 게으른 철수는 비밀번호를 기억하는 것이 너무 귀찮았습니다.
적어서 가지고 다니고 싶지만 누가 볼까봐 걱정입니다. 한가지 생각을 해냅니다.
0~9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍들을 소거하고 남은 번호를 비밀번호로 만드는 것입니다.
번호 쌍이 소거되고 소거된 번호 쌍의 좌우 번호가 같은 번호이면 또 소거 할 수 있습니다.
'''
def get_password(n, pwd):
    stack = []
    for num in pwd:
        if len(stack) == 0 or num != stack[-1]:
            stack.append(num)
        else:
            stack.pop()
    return stack

for t in range(1, 11):
    N, password = input().split()
    N = int(N)
    ans = get_password(N, password)
    print('#%d %s' % (t, ''.join(ans)))
'''
[입력]
10 1238099084  
16 4100112380990844

[출력]
#1 1234
#2 4123
'''