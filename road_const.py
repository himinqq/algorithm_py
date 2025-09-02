from collections import deque


def solution(board):

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    N = len(board)
    INF = float('inf')

    def bfs(x, y, cost, d):
        dist = [[INF] * N for _ in range(N)]
        dist[0][0] = 0
        q = deque([[x, y, cost, d]])
        while q:
            x, y, c, d = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 1:
                    continue
                if i == d:
                    new_cost = c + 100
                else:
                    new_cost = c + 600
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    q.append([nx, ny, new_cost, i])
        return dist[-1][-1]

    return min(bfs(0, 0, 0, 1), bfs(0, 0, 0, 2))
