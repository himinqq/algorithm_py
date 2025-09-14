import sys

input = sys.stdin.readline
# 같은 원소 K개 이하로 들어있는 최장 연속 부분 수열의 길이
N, K = map(int, input().split())
arr = list(map(int, input().split()))

vis = [0] * (max(arr) + 1)
ans = 0
st = 0
for ed in range(N):
    vis[arr[ed]] += 1

    # 현재 숫자가 K번 초과하면, 윈도우 시작점 오른쪽으로 이동시키기
    while vis[arr[ed]] > K:
        vis[arr[st]] -= 1
        st += 1

    ans = max(ans, ed - st + 1)

print(ans)
