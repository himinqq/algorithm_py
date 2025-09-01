N = int(input())
nums = list(map(int,input().split()))

# 연속한 수 1개 이상 뽑았을 때
# 같은 수 여러번 등장하지 않는 경우의 수


st, ed = 0, 0
ans = 0
vis = [False] * (N+1)

while st <= ed < N:

    if not vis[nums[ed]]:
        vis[nums[ed]] = True
        ed += 1
        ans += ed - st

    else: # 같은 수 생기면
        while vis[nums[ed]]: # 같은 수 만날 때 까지 st 옮기기
            vis[nums[st]] = False
            st += 1

print(ans)




