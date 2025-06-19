import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
v,e = map(int,input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
dist = [INF]* (v+1)

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0

    while q:
        cur_dist, node = heapq.heappop(q)

        if dist[node] < cur_dist:
            continue

        for adj in graph[node]:
            cost = cur_dist + adj[1]
            if cost < dist[adj[0]]:
                dist[adj[0]] = cost
                heapq.heappush(q,(cost,adj[0]))

dijkstra(k)

for d in range(1,len(dist)):
    if dist[d] == INF:
        print("INF")
    else:
        print(dist[d])