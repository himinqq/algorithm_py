import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
fireballs = deque()
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r - 1, c - 1, m, s, d])
for _ in range(K):
    board = [[[] for _ in range(N)] for _ in range(N)]

    # 1. 파이어볼 모두 이동
    while fireballs:
    # 파이어볼을 fireballs에서 하나씩 꺼내서 새 위치 계산 후 board[nr][nc]에 기록
        r, c, m, s, d = fireballs.popleft()
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        board[nr][nc].append((m, s, d))

    # 2. 이동 후 같은 칸 처리
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                continue
            # 처리 결과로 생성된 새 파이어볼을 fireballs 큐에 다시 저장
            if len(board[i][j]) == 1:
                fireballs.append((i, j, *board[i][j][0]))
            else:
                new_m = sum(m for m, s, d in board[i][j]) // 5
                new_s = sum(s for m, s, d in board[i][j]) // len(board[i][j])
                if new_m == 0:
                    continue  # 질량 0이면 소멸
                directions = [d % 2 for m, s, d in board[i][j]]
                if all(d == directions[0] for d in directions): # 첫번째 기준으로 모두 짝수이거나 홀수인지 확인
                    new_d = [0, 2, 4, 6]
                else:
                    new_d = [1, 3, 5, 7]
                for nd in new_d:
                    fireballs.append((i, j, new_m, new_s, nd))
print(sum(m for r, c, m, s, d in fireballs))
