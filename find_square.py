def solution(board):
    answer = 0
    dp = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    dp[0] = board[0]
    for row in range(len(board)):
        dp[row][0] = board[row][0] # 첫 행, 첫 열은 단순히 복사 (초기화)

    #
    for row in range(0, len(dp)):
        for col in range(0, len(dp[0])):
            # (i,j)가 1일 때, 세 방향 중 가장 작은 정사각형에 1 더해서 새로운 정사각형 생성
            if (row - 1 >= 0) and (col - 1 >= 0) and board[row][col] == 1:
                dp[row][col] = min(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1]) + 1

    for i in range(len(dp)):
        temp = max(dp[i])
        answer = max(answer, temp)

    return answer * answer