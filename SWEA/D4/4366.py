'''
4366. 정식이의 은행 업무

삼성은행의 신입사원 정식이는 실수를 저질렀다.
은행 업무가 마감되기 직전인 지금, 송금할 금액을 까먹고 말았다.
하지만 다행스럽게도 정식이는 평소 금액을 2진수와 3진수의 두 가지 형태로 기억하고 다니며, 
기억이 명확하지 않은 지금조차 2진수와 3진수 각각의 수에서 단 한 자리만을 잘못 기억하고 있다는 것만은 알고 있다. 
예를 들어 현재 기억이 2진수 1010과 3진수 212을 말해주고 있다면 이는 14의 2진수인 1110와 14의 3진수인 112를 잘못 기억한 것이라고 추측할 수 있다.
정식이는 실수를 바로잡기 위해 당신에게 부탁을 하였다.
정식이가 송금액을 추측하는 프로그램을 만들어주자.
( 단, 2진수와 3진수의 값은 무조건 1자리씩 틀리다.  추측할 수 없는 경우는 주어지지 않는다. )
'''
# def bin_to_dec(arr):
#     dec = []
#     for i in range(len(arr)):
#         binary = ''
#         for j in range(len(arr)):
#             if i == j:
#                 binary += ('0' if int(arr[j]) else '1')
#             else:
#                 binary += arr[j]
#         dec.append(int(binary, 2))
#     return dec

# def get_ans(arr, base):
#     idx = 0
#     while idx < len(arr):
#         tri_list = list(arr)
#         for i in range(3):
#             tri_list[idx] = str(i)
#             print(tri_list)
#             num = int(''.join(tri_list), 3)
#             if num in base:
#                 return num
#         idx += 1
#     return 0

# T = int(input())
# for t in range(1, T+1):
#     two = input()
#     three = input()
#     # 이진수에서 가능한 숫자 목록
#     bin_list = bin_to_dec(two)
#     # 3진수에서 가능한 목록과 비교
#     ans = get_ans(three, bin_list)
#     print('#%d %d' % (t, ans))

def check(b_idx, t_idx):
    b_change = '0' if int(two[b_idx]) else '1'
    b_num = int(two[:b_idx] + b_change + two[b_idx+1:], 2)
    for i in range(3):
        t_change = str(i)
        if three[t_idx] == t_change:
            continue
        t_num = int(three[:t_idx] + t_change + three[t_idx+1:], 3)
        if b_num == t_num:
            return b_num
    return 0

def get_ans():
    for i in range(len(two)):
        for j in range(len(three)):
            same_num = check(i, j)
            if same_num:
                return same_num
    return 'No result'

T = int(input())
for t in range(1, T+1):
    two = input()
    three = input()
    # 2진수 한 자리 바꾼거에서 3진수 바꾼 거 체크..?
    ans = get_ans()
    print('#%d %d' % (t, ans))
'''
[입력]
1
1010
212

[출력]
#1 14
'''