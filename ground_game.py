def solution(land):
    length = len(land)

    # dp[i][j] : i행 j열 밟았을 때 최대 점수
    dp = [[0 for _ in range(4)] for _ in range(length)]

    # 첫 줄은 그대로
    dp[0] = land[0][:]

    # 1행부터 마지막 행까지 반복
    for i in range(1, length):
        for j in range(4):  # 0~3열
            # 같은 열은 제외하고 이전 행에서 최댓값 찾기
            max_prev = max(dp[i-1][k] for k in range(4) if k != j)

            # 그 최댓값 + 현재 칸의 점수 = 현재 위치의 누적 최대 점수
            dp[i][j] = land[i][j] + max_prev

    # 마지막 행에서 가장 큰 점수가 전체 최댓값
    return max(dp[-1])

# 1차원 DP
def solution2(land):
    dp = land[0][:]  # 첫 줄 복사

    for i in range(1, len(land)):
        prev_dp = dp[:]  # 이전 행 상태 저장

        for j in range(4):
            # 현재 dp[j]는 이전 줄에서 j가 아닌 나머지 중 최대 + 현재 점수
            dp[j] = land[i][j] + max(prev_dp[k] for k in range(4) if k != j)

    return max(dp)
