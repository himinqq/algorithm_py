import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

f_info = [list(map(int, input().split())) for _ in range(4)]
board = [[[] for _ in range(4)] for _ in range(4)]

for i in range(4):
    for j in range(4):
        num, d = f_info[i][j * 2], f_info[i][j * 2 + 1] - 1
        board[i][j] = [num, d]


def find_fish(bd, target):
    for i in range(4):
        for j in range(4):
            if bd[i][j] and bd[i][j][0] == target:
                return i, j, bd[i][j][1]
    return None


def fish_move(bd, sx, sy):
    for i in range(1, 17):
        fish = find_fish(bd, i)
        if not fish:
            continue
        x, y, d = fish
        for r in range(8):
            nd = (d + r) % 8
            nx, ny = x + dx[nd], y + dy[nd]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:  # 이동 불가능한 조건 필터링
                continue
            if nx == sx and ny == sy:
                continue
            bd[x][y][1] = nd
            bd[nx][ny], bd[x][y] = bd[x][y], bd[nx][ny]
            break


def shark_move(bd, x, y, d):
    fish_loc = []
    for i in range(1, 4):
        nx, ny = x + dx[d] * i, y + dy[d] * i
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
            continue
        if not bd[nx][ny]:
            continue
        fish_loc.append((nx, ny))
    return fish_loc


answer = 0


def dfs(bd, x, y, total):
    global answer
    bd = copy.deepcopy(bd)
    fish_num, d = bd[x][y]
    bd[x][y] = []
    total += fish_num

    fish_move(bd, x, y)

    fishes = shark_move(bd, x, y, d)
    if not fishes:
        answer = max(answer, total)
        return

    for nx, ny in fishes:
        dfs(bd, nx, ny, total)


dfs(board, 0, 0, 0)

print(answer)
