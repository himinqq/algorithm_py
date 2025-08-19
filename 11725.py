import sys

sys.setrecursionlimit(10**6)
N = int(input())
graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(cur):
    for nxt in graph[cur]: # 현재 노드와 연결된 모든 노드 탐색
        # 다음 노드가 현재 노드의 부모인 경우 건너 뛰기
        # 자식노드에서 부모 노드로 역방향 탐색 막기
        # 트리는 양방향 간선으로 입력되지만, DFS를 돌 때는 한 방향(부모 → 자식) 으로만 내려가야 하기 때문
        if parent[cur] == nxt:
            continue
        parent[nxt] = cur # nxt의 부모는 cur
        dfs(nxt)
dfs(1)

for node in range(2,N+1):
    print(parent[node])

