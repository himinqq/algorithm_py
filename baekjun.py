import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

def make_tree(cur,parent):
    for nxt in graph[cur]:
        if nxt != parent:
            tree[cur].append(nxt)
            make_tree(nxt,cur)

def count_node(cur):
    for nxt in tree[cur]:
        count_node(nxt)
        size[cur] += size[nxt]

# 정점 수, 루트번호, 쿼리 수
n, r, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
tree = [[] for _ in range(n + 1)]
make_tree(r, -1)
size = [1] * (n + 1) # 자기자신 포함해야 하므로 1로 초기화
count_node(r)

# 정점 u를 루트로 하는 서브트리에 속한 정점 수 출력
for i in range(q):
    u = int(input())
    print(size[u])