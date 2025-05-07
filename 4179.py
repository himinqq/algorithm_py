##: 벽
#.: 지나갈 수 있는 공간
#J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
#F: 불이 난 공간
import sys
from collections import deque

#지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.
#지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.

#4 4
####
#JF#
#..#
#..#
#3

#불은 상하좌우로 벽제외하고 퍼짐
#지훈이는 불이 퍼지기 전에 . 으로 이동해야됨
#지훈이가 범위 벗어나는 순간 flg = 탈출

n,m = map(int,input().split())

graph = [list(input().strip()) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

jhDis = [[-1]*m for _ in range(n)] #지훈 도착 시간
fDis = [[-1]*m for _ in range(n)] #불 도착 시간
jq = deque()
fq = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'J':
            jq.append((i,j))
            jhDis[i][j] = 0
        if graph[i][j] == 'F':
            fq.append((i,j))
            fDis[i][j] = 0
#불에 대한 bfs
while fq:
    currX, currY = fq.popleft()
    for i in range(4):
        nx = currX + dx[i]
        ny = currY + dy[i]
        if nx <0 or nx>= n or ny<0 or ny>=m:
            continue
        if graph[nx][ny] == '#' or fDis[nx][ny] >=0:
            continue
        fq.append((nx,ny))
        fDis[nx][ny] = fDis[currX][currY] + 1

#지훈에 대한 bfs
while jq:
    currX, currY = jq.popleft()
    for i in range(4):
        nx = currX + dx[i]
        ny = currY + dy[i]
        #범위 벗어나면 지훈이 탈출한 것
        if nx <0 or nx >=n or ny <0 or ny >=m:
            print(jhDis[currX][currY]+1)
            sys.exit(0)
        #벽이거나 방문한적 있으면 건너뛰기
        if graph[nx][ny] == '#' or jhDis[nx][ny] >= 0:
            continue
        #불이 도착하는 시간(nx,ny)이 지훈이가 도착하는 시간(currX,currY)+1 보다 작거나 같으면 지나갈 수 없음
        #불이 먼저 붙었거나, 같은 시간에 도달
        if fDis[nx][ny] != -1 and fDis[nx][ny] <= jhDis[currX][currY]+1:
            continue
        jhDis[nx][ny] = jhDis[currX][currY] + 1
        jq.append((nx,ny))

print("IMPOSSIBLE")




