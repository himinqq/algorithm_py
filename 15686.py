
from itertools import combinations

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]
homes = []
chickens = []

def cal_dis(chickens):
    tot = 0
    for hx, hy in homes:
        dist = min(abs(hx-cx)+ abs(hy-cy) for cx,cy in chickens)
        tot += dist
    return tot

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            homes.append((i,j))
        elif city[i][j] == 2:
            chickens.append((i,j))

min_dis = int(1e9)

for comb in combinations(chickens,m):
    min_dis = min(min_dis,cal_dis(comb))

print(min_dis)