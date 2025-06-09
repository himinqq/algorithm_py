n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cross = list(zip(*board))


def find(ways):
    vis = [False] * n

    for i in range(1,n):
        diff = ways[i] - ways[i - 1]
        if abs(diff) > 1:
            return False
        if diff == 1:  # 오르막 2 2 3
            for j in range(l):  # 경사로 길이만큼 확인
                if i - j - 1 < 0 or ways[i - 1] != ways[i - j - 1] or vis[i - j - 1]:
                    return False
                if ways[i - 1] == ways[i - j - 1]:  # 좌우 높이 같으면 경사로 놓기
                    vis[i - j - 1] = True
        elif diff == -1:  # 내리막 3 3 2 2
            for j in range(l):
                if i + j >= n or ways[i] != ways[i + j] or vis[i + j]:
                    return False
                if ways[i] == ways[i + j]:
                    vis[i + j] = True
    return True


result = 0
for i in range(n):
    if find(board[i]):
        result += 1
    if find(cross[i]):
        result += 1
print(result)
