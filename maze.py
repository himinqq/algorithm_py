import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def get_dist(map, x, y):
    ROW, COL = len(map), len(map[0])
    dist = [[-1] * COL for _ in range(ROW)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= ROW or ny < 0 or ny >= COL:
                continue
            if dist[nx][ny] >= 0 or map[nx][ny] == 'X':
                continue
            q.append((nx, ny))
            dist[nx][ny] = dist[cx][cy] + 1
    return dist


def solution(maps):
    answer = 0
    ROW, COL = len(maps), len(maps[0])
    sx, sy = 0, 0
    ex, ey = 0, 0
    lx, ly = 0, 0
    for i in range(ROW):
        for j in range(COL):
            if maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'E':
                ex, ey = i, j
            elif maps[i][j] == 'L':
                lx, ly = i, j
    dist_s = get_dist(maps, sx, sy)
    to_lever = dist_s[lx][ly]
    if to_lever == -1:
        return -1

    dist_l = get_dist(maps, lx, ly)
    to_exit = dist_l[ex][ey]
    if to_exit == -1:
        return -1
    return to_lever + to_exit
