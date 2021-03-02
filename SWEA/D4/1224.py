'''
1224. 계산기3

문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.
예를 들어 “3+(4+5)*6+7” 라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
"345+6*+7+"
변환된 식을 계산하면 64를 얻을 수 있다.
문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 문자열 중간에 괄호가 들어갈 수 있다.
이 때 괄호의 유효성 여부는 항상 옳은 경우만 주어진다.
피연산자인 숫자는 0 ~ 9의 정수만 주어진다.
'''
def get_postfix(infix):
    stack = []
    postfix = ''
    for token in infix:
        if token.isdigit():
            postfix += token
        elif token == ')':
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            if not stack or icp.get(token) > isp.get(stack[-1]):
                stack.append(token)
            else:
                while stack and icp.get(token) <= isp.get(stack[-1]):
                    postfix += stack.pop()
                stack.append(token)
    while stack:
        postfix += stack.pop()
    return postfix

calc = {'+': (lambda a, b: a+b),
        '*': (lambda a, b: a*b)}

def calculation(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        else:
            stack.append(calc[token](stack.pop(), stack.pop()))
    return stack

# in-stack priority
isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
# in-coming priority
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

for t in range(1, 11):
    N = int(input())
    infix_notation = input()
    postfix_notation = get_postfix(infix_notation)
    ans = calculation(postfix_notation)
    print('#%d %s' % (t, *ans))