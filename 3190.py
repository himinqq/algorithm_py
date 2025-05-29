from collections import deque

n = int(input())

# 사과의 개수
k = int(input())

board = [[0]* n for _ in range(n)]

for _ in range(k):
    x,y = map(int,input().split())
    board[x-1][y-1] = 8

# 뱀의 방향 (시간, 방향)
l = int(input())
rotations = dict()
for _ in range(l):
    t, d = input().split()
    rotations[int(t)] = d

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
direction = 0

snake = deque()
snake.append((0,0))
board[0][0] = 2

time = 0
while True:
    time += 1
    head_x, head_y = snake[-1]

    nx = head_x + dx[direction]
    ny = head_y + dy[direction]

    #벽, 자기자신 몸통과 부딪히면 종료
    if nx<0 or nx>=n or ny<0 or ny>=n or board[nx][ny] == 2:
        break

    # 사과 있는 경우
    if board[nx][ny] == 8:
        board[nx][ny] = 2
        snake.append((nx, ny))
    else:
        board[nx][ny] = 2
        snake.append((nx, ny))
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0

    if time in rotations:
        if rotations[time] == 'L':
            direction = (direction -1)%4
        else:
            direction = (direction+1) % 4

print(time)

