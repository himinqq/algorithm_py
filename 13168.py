FREE = {"Mugunghwa", "ITX-Saemaeul", "ITX-Cheongchun"}  # 무료
HALF = {"S-Train", "V-Train"} # 50% 할인
N, R = map(int, input().split())
cities = list(input().split())
city_idx = {name: i for i, name in enumerate(cities)}

M = int(input())
plan = list(input().split())

K = int(input())
INF = float('inf')
normal = [[INF] * N for _ in range(N)]
nailro = [[INF] * N for _ in range(N)]
for i in range(N):
    normal[i][i] = nailro[i][i] = 0

for _ in range(K):
    kind, s, e, cost = input().split()
    u, v, c = city_idx[s], city_idx[e], int(cost)

    normal[u][v] = normal[v][u] = min(normal[u][v], c)

    if kind in FREE:
        c_discount = 0
    elif kind in HALF:
        c_discount = c / 2
    else:
        c_discount = c
    nailro[u][v] = nailro[v][u] = min(nailro[u][v], c_discount)

for k in range(N):
    for i in range(N):
        for j in range(N):
            normal[i][j] = min(normal[i][j], normal[i][k]+normal[k][j])
            nailro[i][j] = min(nailro[i][j], nailro[i][k] + nailro[k][j])

trip_normal = 0
trip_nailro = 0
for a,b in zip(plan,plan[1:]):
    u,v = city_idx[a], city_idx[b]
    trip_normal += normal[u][v]
    trip_nailro += nailro[u][v]
if trip_nailro + R < trip_normal:
    print("Yes")
else:
    print("No")