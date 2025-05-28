# 도형 놓으면서 최대가 되는 값 찾기
# 1개의 도형은 4가지 방향 가질 수 있음

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

def rotate(tetromino):
    return [list(row) for row in zip(*tetromino[::-1])]


def flip(tetromino):
    return [row[::-1] for row in tetromino]


tetromino = {
    1: [[1, 1, 1, 1]],
    2: [[1, 1], [1, 1]],
    3: [[1, 0], [1, 0], [1, 1]],  # 대칭
    4: [[1, 0], [1, 1], [0, 1]],  # 대칭
    5: [[1, 1, 1], [0, 1, 0]],
    6: flip([[1, 0], [1, 0], [1, 1]]),
    7: flip([[1, 0], [1, 1], [0, 1]])
}


def attach(x, y, tetro):
    score = 0
    row, col = len(tetro), len(tetro[0])
    for i in range(row):
        for j in range(col):
            nx,ny = i+x, j+y
            if nx<0 or ny<0 or nx>=n or ny>=m:
                return -1
            if tetro[i][j] == 1:
                score += board[nx][ny]
    return score

max_score = 0

for i in range(1,len(tetromino)+1):
    tet = tetromino[i]
    for _ in range(4):
        for x in range(n):
            for y in range(m):
                score = attach(x, y, tet)
                max_score = max(max_score, score)
        tet = rotate(tet)
print(max_score)
