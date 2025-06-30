import sys

input = sys.stdin.readline
n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cross = list(zip(*board))


def check_road(road):
    vis = [False] * n

    for i in range(1, n):
        diff = road[i] - road[i - 1]
        if abs(diff) > 1:
            return False

        if diff == 1:  # 1>2
            base = road[i - 1]
            for j in range(l):
                prev_idx = i - j - 1
                if prev_idx < 0 or base != road[prev_idx] or vis[prev_idx]:
                    return False
                vis[prev_idx] = True

        elif diff == -1:  # 2>1
            base = road[i]
            for j in range(l):
                nxt_idx = i + j
                if nxt_idx >= n or base != road[nxt_idx] or vis[nxt_idx]:
                    return False
                vis[nxt_idx] = True
    return True


result = 0
for i in range(n):
    if check_road(board[i]):
        result += 1
    if check_road(cross[i]):
        result += 1
print(result)
