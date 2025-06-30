com_n = int(input())
pair_m = int(input())
graph = [[] for _ in range(com_n+1)]

for _ in range(pair_m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


vis = [False] * (com_n+1)

def dfs(start):
    vis[start] = True
    for adj in graph[start]:
        if not vis[adj]:
            dfs(adj)

dfs(1)
print(vis.count(True) -1)