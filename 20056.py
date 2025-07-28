from collections import deque

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fireballs = deque()

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r - 1, c - 1, m, s, d))

for _ in range(K):
    grid = [[[] for _ in range(N)] for _ in range(N)]

    # 파이어볼 이동
    while fireballs:
        r, c, m, s, d = fireballs.popleft()
        nr = (r + dr[d] * s) % N # 격자 벗어나면 안으로
        nc = (c + dc[d] * s) % N
        grid[nr][nc].append((m, s, d))

    # 파이어볼 처리
    for i in range(N):
        for j in range(N):
            if not grid[i][j]:
                continue

            if len(grid[i][j]) == 1:
                fireballs.append((i, j, *grid[i][j][0]))
            else:
                total_m = sum(m for m, s, d in grid[i][j])
                total_s = sum(s for m, s, d in grid[i][j])
                count = len(grid[i][j])
                new_m = total_m // 5

                if new_m == 0:
                    continue

                new_s = total_s // count
                directions = [d % 2 for m, s, d in grid[i][j]]
                # 모두 짝수 또는 홀수인지 확인하기 (모든 방향의 홀짝 여부를 확인하기 위해 맨 첫 번째 값 기준으로 둠)
                if all(d == directions[0] for d in directions):
                    new_dirs = [0, 2, 4, 6]
                else:
                    new_dirs = [1, 3, 5, 7]

                for nd in new_dirs:
                    fireballs.append((i, j, new_m, new_s, nd))

# 남아있는 파이어볼 질량 총합
print(sum(m for r, c, m, s, d in fireballs))
