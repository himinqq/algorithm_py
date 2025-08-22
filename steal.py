def solution(money):

    n = len(money)

    # 원형 마을 > 인접한 두 집은 털 수 없음
    # 첫번째 마을 선택한 경우 (마지막 마을 선택 못함)
    dp1 = [0] + money[:-1]

    for i in range(2,n):
        dp1[i] = max(dp1[i-1], dp1[i]+dp1[i-2])

    # 첫번째 마을 선택 안한 경우 (마지막 마을 선택 가능)
    dp2 = [0] + money[1:]
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i] + dp2[i - 2])

    return max(dp1[-1],dp2[-1])
