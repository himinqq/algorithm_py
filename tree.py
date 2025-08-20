def dfs(v, parent):
    vis[v] = True
    for adj in graph[v]:
        if not vis[adj]:
            if dfs(adj,v):
                return True
        elif adj != parent:
            return True
    return False


n, m = map(int, input().split())
NO = "No trees."
ONE = "There is one tree."
LOT = "A forest of {} trees."
CASE = "Case {}: "
idx = 1

while n != 0 or m != 0:
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    vis = [False] * (n + 1)
    cnt = 0
    for node in range(1, n + 1):
        if not vis[node]:
            if not dfs(node,-1):
                cnt += 1

    if cnt == 0:
        print(CASE.format(idx) + NO)
    elif cnt == 1:
        print(CASE.format(idx) + ONE)
    else:
        print(CASE.format(idx) + LOT.format(cnt))
    idx += 1
    n, m = map(int, input().split())