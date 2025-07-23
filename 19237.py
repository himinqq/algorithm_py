import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
directions = list(map(int, input().split()))
priority = {i: [] for i in range(1, m+1)}
for s in range(1, m+1):
    priority[s] = [list(map(lambda x: int(x)-1, input().split())) for _ in range(4)]

# smell[x][y] = [상어번호, 남은시간]
smell = [[[0, 0] for _ in range(n)] for _ in range(n)]

# sharks[s] = [x, y, direction]
sharks = {}
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            s = board[i][j]
            sharks[s] = [i, j, directions[s-1] - 1]

time = 0


def spread_smell():
    for s, (x, y, _) in sharks.items():
        smell[x][y] = [s, k]


def decrease_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0: # 냄새 없어지는 시간 되면
                    smell[i][j][0] = 0 # 번호도 0으로 갱신


def move_sharks():
    global sharks
    # 위치 기준 딕셔너리 > 한 칸에 여러마리 상어 있는지 확인하기 위해
    # key: 상어가 이동하려는 위치 (nx, ny), value: 해당 위치에 들어간 상어 번호 (s)
    new_positions = dict()
    for s in sorted(sharks.keys()): # 작은 상어부터 순서대로
        if s not in sharks: # 상어 방출되고 없으면, 다음 상어 탐색
            continue
        x, y, d = sharks[s]

        found = False
        for nd in priority[s][d]: # 빈 칸 있는 경우
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < n and 0 <= ny < n and smell[nx][ny][0] == 0:
                sharks[s] = [nx, ny, nd] # 우선순위 순서대로 위치 바로 갱신
                found = True
                break

        if not found:
            for nd in priority[s][d]: # 빈칸 없으면 자신의 냄새 있는 칸으로 이동
                nx, ny = x + dx[nd], y + dy[nd]
                if 0 <= nx < n and 0 <= ny < n and smell[nx][ny][0] == s:
                    sharks[s] = [nx, ny, nd]
                    break

        nx, ny, nd = sharks[s]
        if (nx, ny) in new_positions:
            if new_positions[(nx, ny)] < s: # 기존에 있던 상어 번호가 더 작으면
                del sharks[s] # 현재 상어 방출
            else:
                del sharks[new_positions[(nx, ny)]]
                new_positions[(nx, ny)] = s
        else:
            new_positions[(nx, ny)] = s


while True:
    spread_smell()
    move_sharks()
    decrease_smell()
    time += 1

    if len(sharks) == 1:
        print(time if time <= 1000 else -1)
        break
    if time >= 1000:
        print(-1)
        break
