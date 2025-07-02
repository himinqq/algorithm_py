from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 캐릭터가 상대팀 진영에 도착하기 위해 지나가야 하는 칸의 개수 최솟값 리턴
# 만약 도착할 수 없다면 -1 출력

def solution(maps):
    n, m = len(maps), len(maps[0])
    dist = [[-1] * m for _ in range(n)]
    answer = bfs(dist, maps)
    return answer


def bfs(dist, map):
    q = deque([(0, 0)])
    dist[0][0] = 1
    n, m = len(map), len(map[0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny] >= 1 or map[nx][ny] == 0:
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

    return dist[n-1][m-1]
