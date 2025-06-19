import heapq

city_n = int(input())
bus_m = int(input())

INF = int(1e9)

graph = [[] for _ in range(city_n+1)]
dist = [INF] * (city_n+1)
prev = [0] * (city_n+1)  # 경로 추적용

for _ in range(bus_m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

start, end = map(int,input().split())

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
                prev[adj[0]] = node
                heapq.heappush(q,(cost,adj[0]))
dijkstra(start)

path = []
curr = end
while curr != 0:
    path.append(curr)
    curr = prev[curr]
path.reverse()

print(dist[end]) #최소비용
print(len(path)) #도시수
print(*path) #경로

