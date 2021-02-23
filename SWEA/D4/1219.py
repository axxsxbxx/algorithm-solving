'''
1219. 길찾기

그림과 같이 도식화한 지도에서 A도시에서 출발하여 B도시로 가는 길이 존재하는지 조사하려고 한다.
길 중간 중간에는 최대 2개의 갈림길이 존재하고, 모든 길은 일방 통행으로 되돌아오는 것이 불가능하다.
다음과 같이 길이 주어질 때, A도시에서 B도시로 가는 길이 존재하는지 알아내는 프로그램을 작성하여라.

 - A와 B는 숫자 0과 99으로 고정된다.
 - 모든 길은 순서쌍으로 나타내어진다. 위 예시에서 2번에서 출발 할 수 있는 길의 표현은 (2, 5), (2, 9)로 나타낼 수 있다.
 - 가는 길의 개수와 상관없이 한가지 길이라도 존재한다면 길이 존재하는 것이다.
 - 단 화살표 방향을 거슬러 돌아갈 수는 없다.
'''
def find_route(edge):
    # 인접 리스트 생성
    AL = [[] for _ in range(SIZE)]
    for start, end in edge:
        AL[start].append(end)
    # DFS
    stack = [0]
    visited = [0] * SIZE
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = 1
            for n in AL[node]:
                if not visited[n]:
                    if n == 99:
                        return 1
                    stack.append(n)
    return 0

SIZE = 100
for _ in range(10):
    # 테스트 케이스 번호, 길의 개수
    t, E = map(int, input().split())
    load = list(map(int, input().split()))
    edges = [(load[i], load[i + 1]) for i in range(0, len(load), 2)]
    ans = find_route(edges)
    print('#%d %d' % (t, ans))