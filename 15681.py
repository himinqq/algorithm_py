import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

# 그래프 간 연결 관계, 루트를 통해 트리 구성 (DFS)
# 양방향 그래프를 부모->자식 방향의 단방향 그래프로 구성하기
def make_tree(graph, cur, parent, tree):
    for i in graph[cur]:
        if i != parent:
            tree[cur].append(i)
            make_tree(graph, i, cur, tree)

# 모든 노드를 루트로 하는 서브트리의 정점 수 구하기
# 재귀적으로 내려가면서 자식들의 크기를 더해 최종적으로 cur의 서브트리 크기 계산
def count_node(tree, cur, size):
    for i in tree[cur]: # cur 노드의 자식 노드들을 순회
        count_node(tree, i, size) # 자식 i의 서브트리 크기 계산
        # 재귀가 끝나고 나면 size[i]에는 자식 i 서브트리의 정점 수가 들어 있음
        size[cur] += size[i] # 자식 서브트리 크기를 부모 cur의 크기에 더함


# 정점 수, 루트번호, 쿼리 수
n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
tree = [[] for _ in range(n + 1)]
make_tree(graph, r, -1, tree)
size = [1] * (n + 1) # 자기자신 포함해야 하므로 1로 초기화
count_node(tree,r,size)

# 정점 u를 루트로 하는 서브트리에 속한 정점 수 출력
for i in range(q):
    u = int(input())
    print(size[u])
