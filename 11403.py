N = int(input())
reach = [list(map(int, input().split())) for _ in range(N)]

# 경로 유무만 확인
for k in range(N):
    for i in range(N):
        for j in range(N):
            # i에서 k로 가는 길이 있고, k에서 j로 가는 길이 있다면, i에서 j로도 갈 수 있다
            if reach[i][k] and reach[k][j]:
                reach[i][j] = 1

for row in reach:
    print(*row)
