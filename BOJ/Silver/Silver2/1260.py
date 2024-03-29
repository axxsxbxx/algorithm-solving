'''
1260. DFS와 BFS

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
V부터 방문된 점을 순서대로 출력하면 된다.
'''
import sys
from collections import deque
input = sys.stdin.readline

def DFS(AL, v):
    visited[v] = True
    for w in AL[v]:
        if not visited[w]:
            dfs_list.append(w)
            DFS(AL, w)

def BFS(AL, V):
    visited = [False] * (N+1)
    visited[V] = True
    queue = deque([V])

    while queue:
        w = queue.popleft()
        for i in AL[w]:
            if not visited[i]:
                visited[i] = True
                bfs_list.append(i)
                queue.append(i)


N, M, V = map(int, input().split())
AL = [[] for _ in range(N+1)]
visited = [False] * (N+1)
dfs_list = [V]
bfs_list = [V]

for _ in range(M):
    s, e = map(int, input().split())
    AL[s].append(e)
    AL[e].append(s)

for line in AL:
    line.sort()

DFS(AL, V)
BFS(AL, V)
print(' '.join(map(str, dfs_list)))
print(' '.join(map(str, bfs_list)))
'''
[입력]
4 5 1
1 2
1 3
1 4
2 4
3 4

[출력]
1 2 4 3
1 2 3 4
'''