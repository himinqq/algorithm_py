treeN, lengthM = map(int, input().split())

heights = list(map(int,input().split()))

start, end = 1, max(heights)

ans = 0

while True:
    if start > end:
        break
    cnt = 0
    mid = (start + end) // 2

    for h in heights:
        if h > mid:
            cnt += h-mid

    if cnt >= lengthM:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)