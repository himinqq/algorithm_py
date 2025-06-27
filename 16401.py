M,N = map(int,input().split())
snaks = list(map(int,input().split()))

start, end = 1, max(snaks)

ans = 0
while True:
    mid = (start + end) // 2
    if start > end:
        break
    cnt = 0
    for snak in snaks:
        cnt += snak // mid
    if cnt >= M:
        ans = mid  # 일단 이 길이는 가능하니까 정답 후보로 저장
        start = mid + 1 #  # 더 큰 길이가 가능한지 탐색
    else: # 조카 수 만큼 나눠줄 수 없음
        end = mid - 1 #길이 줄여서 확인

print(ans)