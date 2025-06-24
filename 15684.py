t,w = map(int,input().split())

trees = [0] + [int(input()) for _ in range(t)]

dp = [[0]*(w+1) for _ in range(t+1)]

for i in range(t+1):
    # 이동횟수 0번인 경우
    # 한 번도 움직이지 않아서, 이전 위치로부터 이동해서 오는 상황 불가능
    if trees[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    # 이동횟수 1번 이상인 경우
    for j in range(1, w+1):
        # 자두 먹을 수 있는 조건
        if trees[i] == 1 and j % 2 == 0: # i 초에 자두가 1번 나무에서 떨어짐 && 이동횟수 짝수
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + 1
        elif trees[i] == 2 and j % 2 != 0: # i 초에 자두가 2번 나무에서 떨어짐 && 이동횟수 홀수
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-1])

print(max(dp[t]))
