def solution(n, money):
    # money 더해서 n 이 되는 경우의 수

    # dp[i]: i원을 만드는 방법의 수
    # dp[0] = 1: 0원을 만드는 방법은 동전을 하나도 사용하지 않는 경우로 1가지
    dp = [1] + [0] * n

    for m in money: # 각 동전 단위를 하나씩 확인
        for i in range(m, n + 1): # 현재 동전 m을 사용해서 i원을 만드는 경우 추가
            dp[i] += dp[i - m]  # i-m원을 만드는 모든 방법에 동전m 추가하면 i원 만들 수 있음

    return dp[n] % 1000000007
