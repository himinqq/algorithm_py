import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 물고기 번호, 방향 입력
fish_info = [list(map(int, input().split())) for _ in range(4)]

# 초기 상태 세팅
board = [[[] for _ in range(4)] for _ in range(4)]
for x in range(4):
    for y in range(4):
        num = fish_info[x][2 * y]
        d = fish_info[x][2 * y + 1] - 1
        board[x][y] = [num, d]

answer = 0

def find_fish(bd,target):
    for i in range(4):
        for j in range(4):
            if bd[i][j] and bd[i][j][0] == target:
                return i,j,bd[i][j][1]
    return None

def move_fishes(bd,sx,sy):
    for num in range(1,17):
        fish = find_fish(bd,num)
        if not fish:
            continue
        x,y,d = fish

        for i in range(8):
            nd = (d+i) % 8
            nx,ny = x+dx[nd], y+dy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx ==sx and ny == sy):
                bd[x][y][1] = nd
                bd[x][y], bd[nx][ny] = bd[nx][ny],bd[x][y]
                break

def get_shark_moves(bd,x,y,d):
    fish_list = []
    for i in range(1,4):
        nx,ny = x+dx[d]*i, y+dy[d]*i
        if 0 <= nx <4 and 0 <= ny < 4 and bd[nx][ny]:
            fish_list.append((nx,ny))
    return fish_list

# 상어가 물고기를 잡아먹는 모든 가능한 경로를 탐색
# 상어가 이동 가능한 모든 경우를 재귀적으로 탐색해서, 최댓값을 answer 에 저장
# total = 지금까지 상어가 먹은 물고기 번호의 합
def dfs(bd,x,y,total):
    global answer

    bd = copy.deepcopy(bd) # 현재 상태 복사
    fish_num, d = bd[x][y] # 현재 칸에 있는 물고기 먹고, 물고기 방향 d 얻음
    total += fish_num # 먹은 물고기 번호 total에 누적
    bd[x][y] = [] # 먹은 칸은 빈칸으로 처리

    move_fishes(bd,x,y) # 모든 물고기들 1번씩 순서대로 이동

    fishes = get_shark_moves(bd,x,y,d) #상어가 이동할 수 있는 칸 확인 (물고기 있는 칸만 가능)

    if not fishes: # 이동 가능한 곳이 없으면, 정답 후보로 기록하고 리턴
        answer = max(answer,total)
        return

    for nx,ny in fishes: # 상어가 이동할 수 있는 모든 칸으로 재귀 진행
        dfs(bd,nx,ny,total)

dfs(board,0,0,0)
print(answer)
