import sys

t = int(input())
from collections import deque
# 체스판의 한 변의 길이
# 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력

dir = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

for _ in range(t):
    n = int(input())
    dist = [[-1] * n for _ in range(n)]
    nowX, nowY = map(int,input().split())
    goalX, goalY = map(int,input().split())

    q = deque()
    dist[nowX][nowY] = 0
    q.append((nowX,nowY))

    while q:
        x,y = q.popleft()
        if x == goalX and y == goalY:
            print(dist[x][y])
            break
        for dx,dy in dir:
            nx = x+dx
            ny = y+dy
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if dist[nx][ny] == -1:
                q.append((nx,ny))
                dist[nx][ny] = dist[x][y] + 1