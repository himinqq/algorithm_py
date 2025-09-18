N, M = map(int, input().split())
# 만들어야 할 최소 통로 길이

parents = [i for i in range(N + 1)]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def calculate_dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 노드번호 맞추기 위해 0번 인덱스 dummy값
graph = [(0,0)]

# 우주신들 좌표
for i in range(N):
    x, y = map(int, input().split())
    graph.append((x,y))

# 이미 연결된 통로
for _ in range(M):
    a, b = map(int, input().split())
    union(a, b) # 미리 같은 집합으로 처리

edges = []
# 가능한 모든 좌표 쌍에 대해 간선 추가 (거리,시작노드,끝노드)
for i in range(1, N+1):
    for j in range(i + 1, N+1):
        edges.append([calculate_dist(graph[i], graph[j]), i, j])
edges.sort()

ans = 0
# 크루스칼 알고리즘 실행
for e in edges:
    cost, a, b = e
    if find(a) != find(b): # 사이클 생기지 않을 경우에만 연결
        union(a,b)
        ans += cost # 비용 추가

print(f"{ans:.2f}")

