n, m, r = map(int,input().split())

items = [0] + list(map(int,input().split()))

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(r):
    a, b, c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c)
    graph[b][a] = min(graph[b][a],c)

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

max_cnt = 0
for a in range(1,n+1):
    item_cnt = 0
    for b in range(1,n+1):
        if graph[a][b] != INF and graph[a][b] <= m:
            item_cnt += items[b]
    max_cnt = max(item_cnt,max_cnt)

print(max_cnt)