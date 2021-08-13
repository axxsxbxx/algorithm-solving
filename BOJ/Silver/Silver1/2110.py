'''
2110. 공유기 설치

도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 
둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

출력
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
'''
import sys
input = sys.stdin.readline

# 집 간 거리를 가지고 이분탐색...?
N, C = map(int, input().split())
home = sorted(list(int(input().strip()) for _ in range(N)))

start = 1
end = home[-1] - home[0]
dist = []

while start <= end:
    # 두 공유기 사이의 거리 mid -- 이 때 몇 개의 공유기 설치 가능?
    mid = (start + end) // 2
    pos = home[0]
    wifi = 1

    for i in range(1, N):
        if home[i] - pos >= mid:
            wifi += 1
            pos = home[i]
    
    # print(wifi)
    # 설치가능한 공유기 수가 C보다 크면 공유기 사이의 거리 증가 가능
    # start를 mid + 1로 해서 이분탐색
    if wifi >= C:
        dist.append(mid)
        start = mid + 1
    # 설치 가능한 공유기 수가 C보다 작으면 공유기 사이의 거리 감소해야 함
    # end를 mid - 1로 해서 이분탐색
    else:
        end = mid - 1

print(max(dist))
'''
[입력]
5 3
1
2
8
4
9

[출력]
3
'''