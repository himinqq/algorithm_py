import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10 ** 8)

# 방향 상수
UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4

# 입력
R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]

# 상어 정보 입력
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1] = (s, d, z)  # (속력, 방향, 크기)

# 현재 열에서 가장 위에 있는 상어 잡기
def catch_shark(col):
    for row in range(R):
        if board[row][col]:
            _, _, size = board[row][col]
            board[row][col] = 0
            return size
    return 0

# 상어 이동 처리
def move_sharks():
    global board
    new_board = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if not board[i][j]:
                continue

            s, d, z = board[i][j]
            ni, nj, nd = get_next_position(i, j, s, d)

            # 겹치는 상어는 큰 상어만 생존
            if new_board[ni][nj]:
                if new_board[ni][nj][2] < z:
                    new_board[ni][nj] = (s, nd, z)
            else:
                new_board[ni][nj] = (s, nd, z)

    board = new_board

# 상어가 다음에 갈 위치 계산
def get_next_position(x, y, s, d):
    if d == UP or d == DOWN:
        cycle = 2 * (R - 1)
        if d == UP:
            s = (2 * (R - 1) - x + s) % cycle
        else:
            s = (x + s) % cycle

        if s >= R:
            return 2 * (R - 1) - s, y, UP
        return s, y, DOWN

    else:  # LEFT or RIGHT
        cycle = 2 * (C - 1)
        if d == LEFT:
            s = (2 * (C - 1) - y + s) % cycle
        else:
            s = (y + s) % cycle

        if s >= C:
            return x, 2 * (C - 1) - s, LEFT
        return x, s, RIGHT

# 메인 루프
answer = 0
for col in range(C):
    answer += catch_shark(col)
    move_sharks()

print(answer)
