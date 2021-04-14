'''
1248. 공통 조상

진 트리에서 임의의 두 정점의 공통 조상 중 가장 가까운 것을 찾으려 한다.
예를 들어, 아래의 이진 트리에서 정점 8과 13의 공통 조상은 정점 3와 1 두 개가 있다.
이 중 8, 13에 가장 가까운 것은 정점 3이다.
정점 3을 루트로 하는 서브 트리의 크기(서브 트리에 포함된 정점의 수)는 8이다.
임의의 이진 트리가 주어지고, 두 정점이 명시될 때 이들의 공통 조상 중 이들에 가장 가까운 정점을 찾고, 
그 정점을 루트로 하는 서브 트리의 크기를 알아내는 프로그램을 작성하라.
입력에서 주어지는 두 정점이 서로 조상과 자손 관계인 경우는 없다.
위의 트리에서 예를 든다면 두 정점이 “11과 3”과 같이 주어지는 경우는 없다.
'''
def get_root(n, arr):
    if parents[n]:
        arr.append(parents[n])
        get_root(parents[n], arr)

def get_tree_size(n):
    global size
    length = len(tree[n])
    size += 1
    for i in range(length):
        get_tree_size(tree[n][i])

T = int(input())
for t in range(1, T+1):
    V, E, a, b = map(int, input().split())
    pc = list(map(int, input().split()))
    # 인덱스가 부모라고 보면된다.
    tree = [[] for _ in range(V+1)]
    # 인덱스가 자식노드라고 보면 된다.
    parents = [0] * (V+1)
    for i in range(0, len(pc), 2):
        parents[pc[i+1]] = pc[i]
        tree[pc[i]].append(pc[i+1])
    # 조상 루트 구하기
    a_root = []
    b_root = []
    get_root(a, a_root)
    get_root(b, b_root)
    # 공통 조상 구하기
    for root in a_root:
        if root in b_root:
            same_root = root
            break
    # 공통 조상의 서브 트리의 크기 구하기
    size = 0
    get_tree_size(same_root)
    print('#%d %d %d' % (t, same_root, size))

'''
[입력]
1
13 12 8 13
1 2 1 3 2 4 3 5 3 6 4 7 7 12 5 9 5 8 6 10 6 11 11 13

[출력]
#1 3 8
'''