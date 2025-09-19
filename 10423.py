import sys

input = sys.stdin.readline

# 발전소와 나머지 모든 도시를 최소 비용으로 연결하기
N, M, K = map(int, input().split())
stations = list(map(int, input().split()))

parents = [0] * (N + 1)

# 발전소 설치된 도시는 0으로 두고, 일반 도시는 자기 자신을 루트로
for i in range(1, N + 1):
    if i in stations:
        continue
    parents[i] = i

edges = []

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


answer = 0
edges.sort() # 간선 비용순으로 정렬

for e in edges:
    cost, a, b = e

    # 서로 다른 집합에 속한 도시면 연결
    # 발전소 있는 도시들은 같은 루트(0)으로 묶여 있으므로, 발전소간 연결은 무시됨
    if find(a) != find(b):
        union(a, b)
        answer += cost

print(answer)

