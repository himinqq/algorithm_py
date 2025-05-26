# 입력
import sys
from collections import deque
from itertools import permutations, product

raw_cube = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]


# 각 층의 4가지 회전 저장
def get_rotate_version(layer):
    version = [layer]
    for _ in range(3):
        layer = [list(row) for row in zip(*layer[::-1])]
        version.append(layer) # 회전된 값 덮어쓰기
    return version


# 5층 각각의 4가지 회전 상태 미리 저장
cube_version = [get_rotate_version(raw_cube[i]) for i in range(5)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

vis = [[[False] * 5 for _ in range(5)] for _ in range(5)]

INF = float('inf')
# BFS 최단 거리 탐색 (0,0,0) > (4,4,4)

def bfs(maze):
    if maze[0][0][0] == 0 or maze[4][4][4] == 0: #시작/도착지점 벽으로 막혀있음
        return INF
    vis = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    q = deque([(0, 0, 0, 0)])
    vis[0][0][0] = True

    while q:
        z, y, x, dist = q.popleft()
        if (z, y, x) == (4, 4, 4):
            return dist
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or nz < 0 or nz >= 5:
                continue
            if maze[nz][ny][nx] == 1 and not vis[nz][ny][nx]:
                q.append((nz,ny,nx, dist + 1))
                vis[nz][ny][nx] = True
    return INF

# 메인 로직: 모든 순열 × 회전 탐색
# 가능한 모든 미로 구조는 층 순서(순열) x 각 층 회전(곱집합)
# 회전은 독립적, 중복 가능
min_dist = INF
for per in permutations(range(5)):
    for rot in product(range(4),repeat=5): #0, 1, 2, 3 중에서 "하나씩"을 5번 선택하는 모든 경우의 수를 생성
        maze = [cube_version[per[i]][rot[i]] for i in range(5)]
        dist = bfs(maze)
        if dist == 12:
            print(12)
            sys.exit()
        min_dist = min(min_dist,dist)

print(min_dist if min_dist < INF else -1)