'''
1242. 암호코드 스캔
'''
decode = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
          '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

def check_ratio(pwd, ratio):
    # 암호 한 글자당 필요한 글자 수 (한 글자는 7비트로 이루어짐)
    nbits = ratio * 7
    # 암호코드 하나에 필요한 전체 글자 수 (암호글자는 8자리로 이루어짐)
    code_len = nbits << 3
    check = pwd[-code_len:]
    result = []
    for i in range(0, len(check), nbits):
        # 한 글자를 이루는 개수를 가져와서, 비율만큼 건너가면서 검사
        number = decode.get(check[i:i+nbits][::ratio], -1)
        if number == -1:
            return 0
        result.append(number)
    return tuple(result)

def decode_pwd(pwd):
    code_set = set()
    while pwd:
        # 비율 1부터 체크 시작
        ratio = 1
        while True:
            pwd = pwd.zfill(ratio*56)
            check = check_ratio(pwd, ratio)
            if check:
                code_set.add(check)
                code_len = (ratio * 7) << 3
                # 검사완료한 코드는 제거한다
                pwd = pwd[:len(pwd)-code_len].rstrip('0')
                break
            ratio += 1
    return code_set

# 검증코드로 검사
def check_pwd(pwd):
    if (sum(pwd[:-1:2]) * 3 + sum(pwd[1::2])) % 10:
        return 0
    return sum(pwd)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    # set으로 입력받고 빈 항목들 제거
    codes = {input()[:M].rstrip('0') for _ in range(N)}
    codes.discard('')

    final_code = set()
    for code in codes:
        # 2진수로 변환하고 오른쪽에 있는 필요 없는 0 제거
        bin_code = bin(int(code, 16))[2:].rstrip('0')
        decode_code = decode_pwd(bin_code)
        final_code = final_code.union(decode_code)

    ans = 0
    for code in final_code:
        ans += check_pwd(code)

    print('#%d %d' % (t, ans))