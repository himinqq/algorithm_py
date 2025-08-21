from collections import deque


def solution(storage, requests):
    n, m = len(storage) + 2, len(storage[0]) + 2
    r, c = len(storage), len(storage[0])
    board = [['-'] * m for _ in range(n)]

    # 보드 초기화
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            board[i][j] = storage[i - 1][j - 1]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def bfs():
        # 외부와 직접적으로 연결된 빈 공간 확인
        # True → 외부랑 연결된 빈 칸, False → 내부 빈 칸이거나 아직 방문 X
        vis = [[False] * m for _ in range(n)]

        # (0,0) 외부를 시작점으로 두고, bfs로 연결된 모든 칸 표시 -> 외부와 연결된 칸 찾기
        # BFS로 도달한 모든 칸 = 외부와 연결된 칸, BFS로 도달하지 못한 칸 = 외부와 연결되지 않은 칸
        vis[0][0] = True
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or vis[nx][ny]:
                    continue
                if board[nx][ny] == '-':
                    q.append((nx, ny))
                    vis[nx][ny] = True
        return vis

    def is_conn_out(x, y, boundary):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if boundary[nx][ny]: # 외부랑 연결된 칸(boundary == True)이 있으면 지게차 접근 가능
                return True
        return False

    boundary = bfs()

    for req in requests:
        alpha = req[0]
        containers = []
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if board[i][j] == alpha:
                    containers.append((i, j))

        picks = []
        if len(req) == 1:  # 지게차 (외부랑 연결된 면이 있는 컨테이너만 제거)
            for cx, cy in containers:
                # 인접 4 면 중에서 외부랑 연결된 칸 1개 이상인지 확인
                if is_conn_out(cx, cy, boundary):
                    picks.append((cx, cy))
            for px, py in picks:
                board[px][py] = '-'

        else:  # 크레인 (모든 컨테이너 꺼내기)
            for cx, cy in containers:
                board[cx][cy] = '-'

        boundary = bfs()

    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] != '-':
                answer += 1

    return answer
