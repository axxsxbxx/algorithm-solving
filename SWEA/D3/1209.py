'''
1209. sum
다음 100X100의 2차원 배열이 주어질 때, 
각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
'''
def get_max(num, max_num):
    if num > max_num:
        return num
    else:
        return max_num

def get_array_max(array):
    max_num = 0
    length = len(array)
    # 각 행과 열의 합
    for i in range(length):
        row_sum = 0
        col_sum = 0
        for j in range(length):
            row_sum += array[j][i]
            col_sum += array[i][j]
        #최댓값 비교
        max_num = get_max(row_sum, max_num)
        max_num = get_max(col_sum, max_num)
    # 대각선의 합
    diagonal_sum1 = 0
    diagonal_sum2 = 0
    for i in range(length):
        diagonal_sum1 += array[i][i]
        diagonal_sum2 += array[i][len(array[i])-1-i]
    max_num = get_max(diagonal_sum1, max_num)
    max_num = get_max(diagonal_sum2, max_num)
    return max_num


for _ in range(10):
    # 테스트 케이스 번호
    t = int(input())
    # 100X100 배열 입력
    arr = [list(map(int, input().split())) for _ in range(100)]
    ans = get_array_max(arr)
    print('#%d %d' % (t, ans))