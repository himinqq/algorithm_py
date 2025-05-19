n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]

def rotate(sticker):
    return [list(row) for row in zip(*sticker[::-1])]  # zip 결과를 다시 list로 감싸야 수정 가능

def can_attach(x, y, sticker, board):
    row, col = len(sticker), len(sticker[0])
    for i in range(row):
        for j in range(col):
            if sticker[i][j] == 1 and board[x + i][y + j] == 1:
                return False
    return True

def attach(x, y, sticker, board):
    row, col = len(sticker), len(sticker[0])
    for i in range(row):
        for j in range(col):
            if sticker[i][j] == 1:
                board[x + i][y + j] = 1

for _ in range(k):
    row, col = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(row)]

    placed = False
    for _ in range(4):  # 회전 4번까지 시도
        row, col = len(sticker), len(sticker[0])
        # 노트북 크기 : nxm 스티커 크기: rxc
        # x,y에 스티커 붙이면 스티커가 차지하는 영역은 (x, y) ~ (x + r - 1, y + c - 1)
        # 노트북 벗어나면 안되므로, (x + r - 1) < n, (y + c - 1) < m
        # 정리하면 x와 y가 가질 수 있는 시작위치는
        # x in range(0, n - r + 1), y in range(0, m - c + 1)
        for x in range(n - row + 1): #범위 제한
            for y in range(m - col + 1):
                if can_attach(x, y, sticker, board):
                    attach(x, y, sticker, board)
                    placed = True
                    break
            if placed:
                break
        if placed:
            break
        sticker = rotate(sticker)  #  회전 결과를 반드시 다시 저장

# 결과 출력
result = sum(row.count(1) for row in board)
print(result)
