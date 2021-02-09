'''
1208. Flatten

한 쪽 벽면에 다음과 같이 노란색 상자들이 쌓여 있다.
높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.
평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 된다.
평탄화 작업을 위해서 상자를 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만큼 옮기는 작업을 한 후 최고점과 최저점의 차이를 반환하는 프로그램을 작성하시오.

가로 길이는 항상 100으로 주어진다.
모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.
덤프 횟수는 1이상 1000이하로 주어진다.
주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).
'''
def get_min_max(numbers):
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num


def get_result(num, height):
    # 덤프 횟수만큼 평탄화 진행
    for dump in range(num):
        max_num, min_num = get_min_max(height)
        height[height.index(max_num)] -= 1
        height[height.index(min_num)] += 1
    # 최종적으로 평탄화 된 것에서 최소, 최대값 구하기
    max_height, min_height = get_min_max(height)
    return max_height - min_height


T = 10
for t in range(1, T+1):
    dump_num = int(input())
    test_case = list(map(int, input().split()))
    ans = get_result(dump_num, test_case)
    print('#%d %d' % (t, ans))

'''
[입력]
2
5 8 3 1 5 6 9 9 2 2 4

[출력]
2
'''