# O(N*log(N)) or O(N)

def solution(A):
    start = []
    end = []
    intersect = 0
    length = len(A)

    for i in range(length):
        start.append(i - A[i]) 
        end.append(i + A[i])
    start.sort()
    end.sort()

    # 겹쳐지는 경우?! 현재 end보다 오른쪽에 end가 위치 or 현재 start보다 왼쪽에 start 위치
    # 정렬하면 end를 기준으로 다른것들은 모두 오른쪽에 위치하게 됨
    # 따라서 start만 고려하면 된다 : start가 end의 왼쪽에 위치하는지만 확인
    # 각각의 end보다 작거나 같은 start의 수 - 자기자신(무조건 start중 하나는 자기 자신의 원) - 이전에 판단한 end의 개수

    j = 0

    for i in range(length):
        while j < length and start[j] <= end[i]:
            j += 1
        intersect += (j - 1 - i)
    
    return -1 if intersect > 10000000 else intersect