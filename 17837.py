
N, K = map(int, input().split())
chess = [[[] for _ in range(N)] for _ in range(N)]
board = [list(map(int, input().split())) for _ in range(N)]
horse = []
# 0흰색 1빨간색, 2파란색
W, R, B = 0, 1, 2
# 방향은 오,왼,위,아래
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

count = 0
for i in range(K):
    x, y, d = map(int, input().split())
    horse.append([x - 1, y - 1, d-1])
    chess[x - 1][y - 1].append(i)


def change_dir(d):
    if d in [0, 2]:
        d += 1
    elif d in [1, 3]:
        d -= 1
    return d


def move(h_idx):
    x, y, d = horse[h_idx]
    nx, ny = x + dx[d], y + dy[d]

    # 경계 밖이거나 파란색이면 방향 반전 후 한번 더 시도
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == B:
        d = change_dir(d) # 방향 반전
        horse[h_idx][2] = d # 말의 방향전환 반영
        nx, ny = x + dx[d], y + dy[d] # 이동위치 다시 계산
        # 방향을 바꿨음에도 여전히 파란색 또는 밖인 경우 → 이동하지 않음
        if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == B:
            return True # 다음 턴 계속 진행 가능 (게임 끝 아님)

    # 현재 위치에서 이동 대상 말(h_idx) 위에 쌓인 말들 확인
    horse_up = []
    for idx, num in enumerate(chess[x][y]):
        if num == h_idx:
            horse_up.extend(chess[x][y][idx:])
            chess[x][y] = chess[x][y][:idx]
            break
    # 이동할 칸이 빨간색(R)이면 말들 순서 뒤집기
    if board[nx][ny] == R:
        horse_up.reverse()

    # 모든 이동하는 말의 위치 갱신 및 이동 대상 칸에 쌓기
    for h in horse_up:
        horse[h][0], horse[h][1] = nx,ny
        chess[nx][ny].append(h)

    # 이동한 칸의 말이 4개 이상 쌓이면 게임 종료 조건 → False 반환
    if len(chess[nx][ny]) >= 4:
        return False

    # 게임 계속 진행
    return True

while True:
    flag = False
    if count > 1000:
        print(-1)
        break
    for i in range(K): # K번 말들 순서대로 이동시키기
        if move(i) == False:
            flag = True
            break
    count += 1
    if flag:
        print(count)
        break
