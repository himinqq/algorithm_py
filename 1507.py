import sys
input = sys.stdin.readline

N = int(input())
# 각 도로별로 최단거리 주어짐
times = [list(map(int, input().split())) for _ in range(N)]

result = 0
redundant = [[False]*N for _ in range(N)]

for k in range(N): # 경유지
    for i in range(N): # 출발지
        for j in range(N): # 도착지
            if i == j or j == k or i == k:  # 자기 자신이거나 불필요한 조합은 건너뜀
                continue
            # k를 거쳐 더 짧은 경로가 존재하면 입력 자체가 잘못된 것
            if times[i][j] > times[i][k] + times[k][j]:
                print(-1)
                sys.exit(0)
            #  최단 거리가 다른 경유지(k)를 거쳐서 만들어질 수 있다면, i <-> j 간 직접 연결 도로는 필요 없음
            if times[i][j] == times[i][k] + times[k][j]:
                redundant[i][j] = True

# 최종적으로 남는 도로만 더하기
# 무방향 그래프이므로 i<j인 경우만 합산
for i in range(N):
    for j in range(i+1, N):
        if not redundant[i][j]:
            result += times[i][j]

print(result)
