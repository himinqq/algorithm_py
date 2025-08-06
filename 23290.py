import copy

f_dx = [0, -1, -1, -1, 0, 1, 1, 1]
f_dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

m, s = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(m)]
graph = [[[] for _ in range(4)] for _ in range(4)]

for x, y, d in fish:
    graph[x - 1][y - 1].append(d - 1)

shark = tuple(map(lambda x: int(x) - 1, input().split()))
smell = [[0] * 4 for _ in range(4)]

def move_fish():
    res = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while tmp[x][y]:
                d = tmp[x][y].pop()
                for i in range(d, d-8, -1):
                    i %= 8
                    nx, ny = x+f_dx[i], y+f_dy[i]
                    if (nx,ny) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        res[nx][ny].append(i)
                        break
                else:
                    res[x][y].append(d)
    return res

def dfs(x,y,depth, cnt, vis):
    # cnt = 상어가 이동하면서 잡아먹을 수 있는 물고기 수

    global max_eat, shark, eat
    if depth == 3:
        if max_eat < cnt:
            max_eat = cnt
            shark = (x,y)
            eat = vis[:]
        return
    for d in range(4):
        nx,ny = x+dx[d], y+dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx,ny) not in vis:
                vis.append((nx,ny))
                dfs(nx,ny,depth+1, cnt+len(tmp[nx][ny]),vis)
                vis.pop()
            else:
                dfs(nx,ny,depth+1,cnt,vis)

for _ in range(s):
    eat = list()
    max_eat = -1

    # 1. 현재 상태의 모든 물고기 복제
    tmp = copy.deepcopy(graph)

    # 2. 복사해둔 tmp 기준으로 물고기 이동 후 갱신
    tmp = move_fish()

    # 3. 상어 이동 (백트래킹)
    dfs(shark[0],shark[1],0,0,list())

    for x, y in eat:
        if tmp[x][y]:
            tmp[x][y] = []
            smell[x][y] = 3

    # 4. 냄새 사라짐
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1

    # 5. 원본에 이동 이후 물고기 위치 복제 (복제마법)
    for i in range(4):
        for j in range(4):
            graph[i][j] += tmp[i][j]


ans = 0
for i in range(4):
    for j in range(4):
        ans += len(graph[i][j])
print(ans)
