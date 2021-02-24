'''
1223. 계산기2

문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.

예를 들어 “3+4+5*6+7” 라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
"34+56*+7+" 변환된 식을 계산하면 44를 얻을 수 있다.

문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.

-> 변형해서 괄호와 사칙연산을 포함하는 계산기 만들기
'''
# 후위표기법 구하는 함수
def get_postfix(infix):
    stack = []
    postfix = ''
    for token in infix:
        # 토큰이 피연산자면 후위표기법 결과에 바로 저장
        if token.isdigit():
            postfix += token
        # 토큰이 닫는 괄호이면
        elif token == ')':
            # 여는 괄호를 만날때까지 후위표기법 결과에 저장
            while stack[-1] != '(':
                postfix += stack.pop()
            # 여는 괄호는 pop만 하고 저장하지 않음
            stack.pop()
        else:
            # 토큰이 여는 괄호이거나 stack이 비어있거나 token의 우선순위가 stack의 top보다 높으면
            if token == '(' or not stack or icp.get(token) > isp.get(stack[-1]):
                stack.append(token)
            else:
                # stack의 top 우선순위가 token의 우선순위보다 크거나 같을때까지
                while stack and icp.get(token) <= isp.get(stack[-1]):
                    # 후위표기법 결과에 저장함
                    postfix += stack.pop()
                stack.append(token)
        # print(stack, postfix)
    # 스택에 남아있는 연산자가 있으면 후위표기법에 저장함
    if stack:
        while stack:
            postfix += stack.pop()
    # 후위표기법 리턴
    return postfix

# 후위표기법 연산하는 함수
def calculation(postfix):
    stack = []
    for token in postfix:
        # 피연산자를 만나면 스택에 push
        if token.isdigit():
            stack.append(int(token))
        # 연산자를 만나면 필요한 만큼의 피연산자를 stack에서 pop하여 연산
        else:
            b = stack.pop()
            a = stack.pop()
            # 연산결과를 다시 stack에 push
            stack.append(calc(a, token, b))
    # 수식이 끝나면 마지막으로 stack을 pop하여 출력
    return stack

# 사칙연산 하는 함수
def calc(a, token, b):
    if token == '+':
        return a + b
    elif token == '-':
        return a - b
    elif token == '/':
        return a / b
    else:
        return a * b

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

'''
[입력]
5+(7+4/2*(5-4+5)*1/2+1)

[출력]
19.0
'''