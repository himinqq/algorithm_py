# N개의 정수
# 크기가 양수인 부분 수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
# 크기 n인 수열이면 부분수열은 2^n개

# 각 원소를 포함하거나 제외
# 각 재귀 호출이 지금까지 선택한 원소들의 합 total 과 다음에 처리할 위치 idx 기억
def func(idx, total):
    global ans

    # 모든 원소 확인 했으면
    if idx == n:
        # 합계가 s와 같은지 확인
        if total == s:
            ans += 1
        return

    ## nums[idx]를 포함
    func(idx+1, total + nums[idx])
    ## nums[idx]를 제외
    func(idx+1, total)

# idx =0, total = 0부터 시작
func(0,0)

#s == 0 인 경우, 빈 수열 카운트 빼기
if s == 0:
    ans -= 1

print(ans)
