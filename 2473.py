import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

# 세가지 용액 혼합해서 0에 가깝게 만들기
# 세 용액 값 출력

ans = []
min_s = float('inf')

nums.sort()
for i in range(N - 2):
    fst = nums[i]
    snd, thd = i + 1, N - 1

    while snd < thd:
        s = fst + nums[snd] + nums[thd]
        min_s = min(min_s, abs(s))
        if min_s == abs(s):
            ans = [fst, nums[snd], nums[thd]]
        if s == 0:
            ans = [fst, nums[snd], nums[thd]]
            break
        elif s < 0:  # 오른쪽 탐색
            snd += 1
        else:
            thd -= 1

print(*ans)
