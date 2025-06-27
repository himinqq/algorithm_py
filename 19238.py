from collections import deque
import sys
input = sys.stdin.readline

N, M, fuel = map(int, input().split())

# 지도
arr = [[]]
for _ in range(N):
    arr.append([0]+list(map(int, input().split())))
# 현재 위치
taxi = list(map(int, input().split()))

# 사람들 정보
people = []
for _ in range(M):
    people.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find_person():
    tx, ty = taxi
    dist_map = get_dist(tx, ty)
    people.sort(key=lambda p: (-dist_map[p[0]][p[1]], -p[0], -p[1]))
    sx, sy, ex, ey = people.pop()
    return [sx, sy, ex, ey, dist_map[sx][sy]]


def drive():
    global taxi
    global fuel
    # 택시 > 승객까지 이동
    sx, sy, ex, ey, dist = find_person()
    if dist == -1:
        return False
    fuel -= dist
    if fuel < 0:
        return False
    # 승객 목적지 까지 이동
    used = get_dist(sx, sy)
    if used[ex][ey] == -1:
        return False
    fuel -= used[ex][ey]
    if fuel < 0:
        return False
    fuel += used[ex][ey]*2
    taxi = [ex, ey]
    return True


def get_dist(a, b):
    q = deque()
    q.append((a, b))
    visited = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    visited[a][b] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 < nx <= N and 0 < ny <= N and visited[nx][ny] == -1:
                if not arr[nx][ny]:
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx, ny))
    return visited


for _ in range(M):
    if not drive():
        fuel = -1
        break

print(fuel)