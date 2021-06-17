# 50% -- O(N ** 2)
def solution(A):
    cnt = 0
    length = len(A)
    for i in range(length-1):
        for j in range(i+1, length):
            if A[i] == 0 and A[j] == 1:
                cnt += 1
    if cnt > 1000000000:
        return -1
    return cnt

# 50% -- O(N ** 2)
def solution(A):
    cnt = 0
    length = len(A)
    for i in range(length):
        if A[i] == 0:
            cnt += A[i+1:].count(1)
        if cnt > 1000000000:
            return -1
    return cnt

# 
def solution(A):
    cnt = 0
    find_zero = [i for i, a in enumerate(A) if a == 0]

    for i in find_zero:
        cnt += A[i+1:].count(1)
        if cnt > 1000000000:
            return -1
    
    return cnt