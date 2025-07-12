from collections import deque

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def spread():
    temp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                amount = board[i][j] // 5
                cnt = 0
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        temp[nx][ny] += amount
                        cnt += 1
                board[i][j] -= amount * cnt
    for i in range(R):
        for j in range(C):
            board[i][j] += temp[i][j]

def operate():
    # 반시계방향 회전
    # 아래 -> 위 (아래 칸에 위쪽 칸 값을 복사)
    for i in range(upper-1, 0, -1): board[i][0] = board[i-1][0]
    # 왼쪽 -> 오른쪽 (왼쪽 칸에 오른쪽 칸 값을 복사)
    for j in range(C-1): board[0][j] = board[0][j+1]
    # 위 -> 아래 (위 칸에 아래 칸 값을 복사)
    for i in range(upper): board[i][C-1] = board[i+1][C-1]
    # 오른쪽 -> 왼쪽 (오른쪽 칸에 왼쪽 칸 값 복사)
    for j in range(C-1, 1, -1): board[upper][j] = board[upper][j-1]
    # 공기청정기 바로 오른쪽 자리 초기화
    board[upper][1] = 0

    # 시계방향 회전
    for i in range(lower+1, R-1): board[i][0] = board[i+1][0]
    for j in range(C-1): board[R-1][j] = board[R-1][j+1]
    for i in range(R-1, lower, -1): board[i][C-1] = board[i-1][C-1]
    for j in range(C-1, 1, -1): board[lower][j] = board[lower][j-1]
    board[lower][1] = 0

# 공기청정기 위치 찾기
cleaner = []
for i in range(R):
    if board[i][0] == -1:
        cleaner.append(i)
upper, lower = cleaner[0], cleaner[1]

# 시뮬레이션 T초
for _ in range(T):
    spread()
    operate()

# 남은 미세먼지 계산
result = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            result += board[i][j]
print(result)
