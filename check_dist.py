from collections import deque


def solution(places):
    answer = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]

    n, m = len(places), len(places[0])
    for place in places:
        flag = True
        for x in range(n):
            for y in range(m):
                walls = deque()
                if place[x][y] == 'P':
                    # 바로 옆자리에 사람 있는지 확인
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if place[nx][ny] == 'P':
                            flag = False
                            break
                        if place[nx][ny] == 'X':
                            walls.append((nx, ny))
                        # P O P 같이 빈칸 두고 옆자리 앉은 경우
                        nx, ny = x + dx[i] * 2, y + dy[i] * 2
                        mx, my = x + dx[i], y + dy[i] # 중간 칸 확인
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if place[nx][ny] == 'P' and place[mx][my] != 'X':
                            flag = False
                            break

                    # 대각선에 사람 있는지 확인
                    for i in range(4):
                        nx, ny = x + cx[i], y + cy[i]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if place[nx][ny] == 'P':
                            if (nx, y) in walls and (x, ny) in walls:
                                continue
                            else:
                                flag = False
                                break
                if not flag:
                    break
            if not flag:
                break
        if not flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer
