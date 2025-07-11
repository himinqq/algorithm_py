def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0

    while True:
        remove = set()

        # 1. 제거할 2x2 블록 찾기
        for i in range(m - 1):
            for j in range(n - 1):
                block = board[i][j]
                if block == '.':
                    continue
                if block == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    remove |= {(i, j), (i, j+1), (i+1, j), (i+1, j+1)}

        # 2. 제거할 블록 없으면 종료
        if not remove:
            break

        # 3. 블록 제거
        for x, y in remove:
            board[x][y] = '.'
        answer += len(remove)

        # 4. 중력 적용
        for j in range(n):
            tmp = []
            for i in range(m-1, -1, -1):  # 아래서 위로
                if board[i][j] != '.':
                    tmp.append(board[i][j])
            for i in range(m-1, -1, -1):
                if tmp:
                    board[i][j] = tmp.pop(0)
                else:
                    board[i][j] = '.'

    return answer
