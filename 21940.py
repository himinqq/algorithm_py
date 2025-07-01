n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

k = int(input())  # 준형이와 친구들의 총 인원
city_numbers = list(map(int, input().split()))

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# 조건 만족하는 도시 번호 x 출력 (여러개면 오름차순)
# 왕복시간 계산
def calculate():
    min_time = INF
    result = []
    # 1개의 모임 장소에 대해, 친구들 살고 있는 모든 도시들에 대해 왕복시간 계산
    for dst in range(1, n + 1):
        max_time = 0
        for city in city_numbers:
            if graph[city][dst] == INF or graph[dst][city] == INF:
                max_time = INF
                break
            max_time = max(max_time, graph[city][dst] + graph[dst][city])
        if max_time < min_time: # 최대 왕복시간 중에서 최솟값 찾기
            min_time = max_time
            result = [dst]
        elif max_time == min_time:
            result.append(dst)
    return result


print(*calculate())
