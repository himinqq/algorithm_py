from collections import deque

n = int(input())

ocean = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if ocean[i][j] == 9:
            x,y = i,j

def biteFish(x,y,size):
    q = deque()
    q.append((x,y))
    distance = [[-1] * n for _ in range(n)]
    distance[x][y] = 0
    can_eat = []

    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx,ny = cx+dx[i], cy+dy[i],
            if nx <0 or nx>=n or ny<0 or ny>=n:
                continue
            if distance[nx][ny] >=0:
                continue
            if ocean[nx][ny] <= size:
                q.append((nx,ny))
                distance[nx][ny] = distance[cx][cy] + 1
                if ocean[nx][ny] < size and ocean[nx][ny] != 0:
                    can_eat.append((nx,ny,distance[nx][ny]))
    return sorted(can_eat, key=lambda x: (-x[2],-x[0],-x[1]))

time = 0
eat_count = 0
while True:
    availab_fish = biteFish(x,y,size)
    if len(availab_fish) == 0:
        break
    nx,ny,dist = availab_fish.pop()
    time += dist

    ocean[x][y],ocean[nx][ny] = 0,0
    x,y = nx,ny

    eat_count += 1
    if eat_count == size:
        size += 1
        eat_count = 0

print(time)