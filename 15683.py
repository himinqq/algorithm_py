# 감시
from copy import deepcopy
from itertools import product

# 방향: 남, 동, 북, 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cctv_dir = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

def watch(board, x, y, directions):
    for d in directions:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                break
            if board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                board[nx][ny] = 7

# 입력
n, m = map(int, input().split())
office = []
cctvs = [] #cctv위치와 종류

for i in range(n):
    row = list(map(int,input().split()))
    office.append(row)
    for j in range(m):
        if 1 <= row[j] <= 5:
            cctvs.append((i,j,row[j]))

# 가능한 방향 조합
direction_sets = [cctv_dir[t] for _,_,t in cctvs]

min_blind = int(1e9)

for dirs in product(*direction_sets):
    temp = deepcopy(office)
    for (x,y,t), dir_set in zip(cctvs, dirs):
        watch(temp,x,y,dir_set)
    blind = sum(row.count(0) for row in temp)
    min_blind = min(blind,min_blind)

print(min_blind)