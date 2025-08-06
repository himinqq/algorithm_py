def solution(board):
    o_cnt = sum(row.count('O') for row in board)
    x_cnt = sum(row.count('X') for row in board)

    # 둘의 개수 차이가 정확히 0 또는 1이어야 함
    if x_cnt > o_cnt:  # X가 더 많거나
        return 0
    if o_cnt > x_cnt + 1:  # O가 2개 이상 많으면 잘못된 상태
        return 0

    def is_winner(player):
        # 가로
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
        # 세로
        for j in range(3):
            if all(board[i][j] == player for i in range(3)):
                return True
        # 대각선
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2 - i] == player for i in range(3)):
            return True
        return False

    o_win = is_winner('O')
    x_win = is_winner('X')

    if o_win and x_win: # O와 X 모두 이기는 경우
        return 0
    if o_win and o_cnt != x_cnt + 1: # O가 이겼다면, O 개수 == X 개수 + 1
        return 0
    if x_win and o_cnt != x_cnt: # X가 이겼다면, O 개수 == X 개수
        return 0
    return 1
