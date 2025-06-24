from collections import deque

n, m, v = map(int, input().split())

# 인접 리스트 초기화 (1번 노드부터 사용하므로 n+1)
graph = [[] for _ in range(n + 1)]

# 간선 입력 받아서 양방향 연결
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 번호가 작은 것부터 방문하도록 정렬
for g in graph:
    g.sort()

# DFS 구현
def dfs(graph, v, vis):
    vis[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not vis[i]:
            dfs(graph, i, vis)

# BFS 구현
def bfs(graph, v, vis):
    q = deque([v])
    vis[v] = True
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for i in graph[cur]:
            if not vis[i]:
                q.append(i)
                vis[i] = True

# 실행
vis = [False] * (n + 1)
dfs(graph, v, vis)
print()
vis = [False] * (n + 1)
bfs(graph, v, vis)
