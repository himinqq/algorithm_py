# 각 테스트 케이스
# 첫째 줄에는 빌딩 지도의 너비와 높이 w와 h가 주어진다. (1 ≤ w,h ≤ 1000)
from collections import deque
import sys
input = sys.stdin.readline
# 다음 h개 줄에는 w개의 문자, 빌딩의 지도가 주어진다. (빈칸 없는 문자열)

# '.': 빈 공간
# '#': 벽
# '@': 상근이의 시작 위치
# '*': 불
# 각 지도에 @의 개수는 하나이다. (

# 각 테스트 케이스마다 빌딩을 탈출하는데 가장 빠른 시간을 출력한다.
# 빌딩을 탈출할 수 없는 경우에는 "IMPOSSIBLE"을 출력한다.

# 상근이 bfs로 dis 구하고, 불 dfs 로 dis 구함
# 불이 먼저 도착했으면 상근이가 지나갈 수 없음
# 범위 벗어난 경우 탈출. 모든 반복 이후에도 탈출하지 못하면 impossible

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    #w열 h행
    w, h = (map(int, input().split()))
    graph = [list(input().strip()) for i_ in range(h)]
    disF = [[-1] * w for _ in range(h)]
    disJ = [[-1] * w for _ in range(h)]

    jhQ = deque()
    fQ = deque()

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '*':
                fQ.append((i,j))
                disF[i][j] = 0
            if graph[i][j] == '@':
                jhQ.append((i,j))
                disJ[i][j] = 0
    while fQ:
        x, y = fQ.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == "#" or disF[nx][ny] >= 0:
                continue
            fQ.append((nx, ny))
            disF[nx][ny] = disF[x][y] + 1
    # 상근에 대한 bfs
    flg = False
    while jhQ and not flg:
        x, y = jhQ.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                print(disJ[x][y] + 1)
                flg = True
                break
            if graph[nx][ny] == '#' or disJ[nx][ny] >= 0:
                continue
            if disF[nx][ny] != -1 and (disF[nx][ny] <= disJ[x][y]+1):
                continue
            jhQ.append((nx,ny))
            disJ[nx][ny] = disJ[x][y] + 1
    if not flg:
        print("IMPOSSIBLE")
