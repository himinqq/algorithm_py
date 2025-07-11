from collections import deque
from itertools import combinations

n, virus_num = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

virus_loc = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus_loc.append([i, j])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def spread_virus(virus):
    q = deque()
    dist = [[-1] * n for _ in range(n)]
    for x, y in virus:
        q.append((x, y))
        dist[x][y] = 0

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] != 1 and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[cx][cy] + 1
    max_time = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                if dist[i][j] == -1:
                    return float('inf')
                max_time = max(max_time, dist[i][j])
    return max_time

min_time = float('inf')
for comb in combinations(virus_loc, virus_num):
    time = spread_virus(comb)
    min_time = min(time, min_time)

print(min_time if min_time != float('inf') else -1)
