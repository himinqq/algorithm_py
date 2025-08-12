def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i + 1].append(j + 1)
    vis = [False] * (n + 1)

    def dfs(v):
        vis[v] = True
        for adj in graph[v]:
            if not vis[adj]:
                dfs(adj)

    cnt = 0
    for node in range(1, n + 1):
        if not vis[node]:
            dfs(node)
            cnt += 1

    return cnt
