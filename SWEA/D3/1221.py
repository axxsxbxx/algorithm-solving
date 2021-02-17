'''
1221. GNS

숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.
'''
def num_sort(arr):
    cnt = [0] * 10
    # 들어가 있는 문자 count
    for number in arr:
        for i in range(len(cnt)):
            if number == num[i]:
                cnt[i] += 1

    # sorted_num = []
    # for i in range(len(cnt)):
    #     for n in ([num[i]] * cnt[i]):
    #         sorted_num.append(n)
    # return sorted_num

    sorted_num = []
    for i in range(len(cnt)):
        for _ in range(cnt[i]):
            sorted_num.append(num[i])
    return sorted_num

T = int(input())
num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for _ in range(T):
    t, N = input().split()
    numbers = input().split()
    print('%s' % t)
    print(*num_sort(numbers))