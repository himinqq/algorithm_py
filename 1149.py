# 1-N 집 규칙 만족 하면서 모든 집 칠하는 비용 최소

# 규칙
# 1,2 번 집의 색 달라야 됨
# N번 N-1번 집 색 달라야 됨
# i번 집은 i-1, i+1 집과 달라야 됨
# 3번 연속 집 색 모두 달라야 됨 RGB조합- R/G로 시작

n = int(input())

cost = [[0,0,0]] + [list(map(int,input().split())) for _ in range(n)]

# d[i][j] = i번째 집 색 비용, RGB 색 선택
# d[i][0] = min(d[i-1][1],d[i-1][2]) + R[i](빨강으로 칠할 때 비용)
# d[i][1] = min(d[i-1][0],d[i-1][2]) + G[i]
# d[i][2] = min(d[i-1][0],d[i-1][1]) + B[i]

# 초기값
# d[1][0] = R[1]
# d[1][1] = G[1]
# d[1][2] = B[1]

d = [[0]*3 for _ in range(n+1)]

d[1][0] = cost[1][0]
d[1][1] = cost[1][1]
d[1][2] = cost[1][2]

for i in range(2,n+1):
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + cost[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + cost[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + cost[i][2]

print(min(d[n][0],d[n][1],d[n][2]))