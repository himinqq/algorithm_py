INF = float('inf')
N,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = float('inf')
vis = [False] * (N+1)
def find_route(v,cost,cnt):
    global answer
    if cnt == N:
        answer = min(answer,cost)
        return
    for next in range(N):
        if not vis[next]:
            vis[next] = True
            find_route(next,cost+graph[v][next],cnt+1)
            vis[next] = False

find_route(K,0,0)
print(answer)