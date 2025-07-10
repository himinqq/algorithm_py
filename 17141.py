from collections import deque
from itertools import combinations

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

virus_loc = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus_loc.append([i, j])


def bfs(active):
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    for x, y in active:
        q.append((x, y))
        dist[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] >= 0:
                continue
            if board[nx][ny] != 1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
    max_time = 0
    for i in range(n):
        for j in range(n):
            # 감염되지 않은 빈 칸 또는 '선택되지 않은' 바이러스 칸2
            if board[i][j] != 1 and (i, j) not in active:
                if dist[i][j] == -1:
                    return float('inf')
                max_time = max(max_time, dist[i][j])
    return max_time


min_time = float('inf')
for comb in combinations(virus_loc, m):
    time = bfs(comb)
    min_time = min(min_time, time)

print(min_time if min_time != float('inf') else -1)
