N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0

# 다른 수 두개의 합으로 나타낼 수 있는 수의 개수 찾기
for target_idx in range(N):
    target = arr[target_idx]
    st, ed = 0, N - 1
    while st < ed:

        # 자기자신일 때는 스킵
        if st == target_idx:
            st += 1
            continue
        if ed == target_idx:
            ed -= 1
            continue

        s = arr[st] + arr[ed]
        if s == target:
            ans += 1
            break
        elif s < target:
            st += 1
        else:
            ed -= 1

print(ans)
