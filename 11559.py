from collections import deque

row, col = 12, 6
board = [list(input().strip()) for _ in range(row)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, vis):
    q = deque()
    q.append((x, y))
    vis[x][y] = True
    color = board[x][y]
    group = [(x, y)]

    while q:
        cx, cy = q.popleft()
        for dir in range(4):
            nx = cx + dx[dir]
            ny = cy + dy[dir]
            if nx <0 or nx>=row or ny<0 or ny>=col:
                continue
            if not vis[nx][ny] and board[nx][ny] == color:
                vis[nx][ny] = True
                q.append((nx, ny))
                group.append((nx, ny))
    return group

def update_board(blow_list):
    # 터진 칸은 .dmfh
    for x,y in blow_list:
        board[x][y] = '.'
    #중력 적용
    for y in range(col):
        stack = []
        for x in range(row):
            if board[x][y] != '.':
                stack.append(board[x][y])
        for x in range(row-1,-1,-1):
            board[x][y] = stack.pop() if stack else '.'

def simulate():
    chain = 0
    while True:
        vis = [[False]* col for _ in range(row)]
        blow_list = [] #터트릴 블록 그룹 찾기

        for i in range(row):
            for j in range(col):
                if board[i][j] != '.' and not vis[i][j]:
                    group = bfs(i,j,vis)
                    if len(group) >= 4:
                        blow_list.extend(group)

        if not blow_list:
            break  # 여기! 루프 끝나고 검사해야 함

        update_board(blow_list)
        chain += 1

    return chain


print(simulate())

