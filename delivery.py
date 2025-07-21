import heapq


def solution(N, road, K):
    answer = 0
    INF = float('inf')
    dist = [INF] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    q = []
    heapq.heappush(q, (0, 1))
    dist[1] = 0

    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for adj, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < dist[adj]:
                dist[adj] = new_cost
                heapq.heappush(q, (new_cost, adj))
    print(dist)
    for country in range(1,N + 1):
        if dist[country] < K:
            answer += 1
        print(dist[country], answer, end="  ")
    return answer
