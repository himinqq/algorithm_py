import heapq
import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
graph = [[] for _ in range(N+1)]
INF = float('inf')

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[b].append((a,c))

meeting_room = list(map(int,input().split()))

def dijkstra():
    dist = [INF] * (N+1)
    q = []

    # 모든 시작점 초기화
    for room in meeting_room:
        dist[room] = 0
        heapq.heappush(q,(0,room))

    while q:
        cost,node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for adj, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[adj]:
                dist[adj] = new_cost
                heapq.heappush(q,(new_cost,adj))
    return dist

distances = dijkstra()
max_dist = -1
max_city = -1

for city in range(1,N+1):
    if distances[city] > max_dist:
        max_dist = distances[city]
        max_city = city

print(max_city)
print(max_dist)