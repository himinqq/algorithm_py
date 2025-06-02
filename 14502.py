from collections import deque
from copy import deepcopy
from itertools import combinations, count

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

virus_places = []
wall_places = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus_places.append((i, j))
        elif board[i][j] == 0:
            wall_places.append((i, j))

def bfs(board_w):
    q = deque(virus_places)
    visited = [[False] * m for _ in range(n)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board_w[nx][ny] == 0 and not visited[nx][ny]:
                board_w[nx][ny] = 2  # 바이러스 퍼짐
                q.append((nx, ny))
    # 안전 영역 계산 (== 0의 개수)
    return sum(row.count(0) for row in board_w)

max_safe = 0
for walls in combinations(wall_places, 3):
    tmp_board = deepcopy(board)
    for x, y in walls:
        tmp_board[x][y] = 1  # 벽 세우기
    safe_area = bfs(tmp_board)
    max_safe = max(max_safe, safe_area)

print(max_safe)
