import heapq
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

INF = int(1e9)

def dijkstra(v,dist):
    q = []
    heapq.heappush(q,(0,v))
    dist[v] = 0

    while q:
        cost,node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for adj,adj_cost in graph[node]:
            new_cost = cost + adj_cost
            if new_cost < dist[adj]:
                dist[adj] = new_cost
                heapq.heappush(q,(new_cost,adj))


for _ in range(M):
    u,v = map(int,input().split())
    dist = [INF] * (N + 1)
    dist_from_u = dijkstra(u,dist)
    print(dist[v])
