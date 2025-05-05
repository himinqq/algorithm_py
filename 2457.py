# 3/1 부터 11/30까지는 매일 한가지 이상의 꽃 피어있기
# 선택한 꽃들의 최소 개수 출력
# 3/1 12/1까지 피어있어야 함

# 날짜 비교 편하게 하기 위해 3/1을 301 형식으로 변경
def to_int(m, d):
    return m * 100 + d

ans = 0
idx = 0

n = int(input())
flowers = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    flowers.append((to_int(sm, sd), to_int(em, ed)))

#시작일 오름차순, 종료일 내림차순
flowers.sort(key=lambda x: (x[0], -x[1],))

target_end = to_int(11, 30)
curr_end = to_int(3, 1)

#현재 구간의 끝이 목표 완료일(11/30)보다 작거나 같으면 반복
while curr_end <= target_end:

    nxt_end = curr_end

    #꽃 남아있고, 시작일이 마지막날 이전 이라면 (시작일이 현재 구간에 포함)
    while idx < n and flowers[idx][0] <= curr_end:
        #끝나는 날짜가 더 길면 선택 (현재 구간을 포함하면서, 가장 늦게 까지 피어있는 꽃)
        nxt_end = max(nxt_end, flowers[idx][1])
        idx += 1

    #nxt_end 가 초기값에서 바뀌지 않았으면, 목표 구간까지 도달하지 못한 것
    if nxt_end == curr_end:
        ans = 0
        break

    curr_end = nxt_end
    ans += 1

print(ans)
