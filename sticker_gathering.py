def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]

    dp1 = [0] + sticker[1:]
    dp2 = [0] + sticker[:-1]

    for i in range(2,n):
        dp1[i] = max(dp1[i-1], dp1[i-2]+dp1[i])

    for i in range(2,n):
        dp2[i] = max(dp2[i-1], dp2[i-2]+dp2[i])

    answer = max(dp1[-1], dp2[-1])

    return answer