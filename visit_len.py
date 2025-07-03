# 캐릭터가 처음 걸어본 길이 출력
# 범위 벗어나면 그 명령은 무시
# LR UD 명령으로 이동

cmd = {
    'R': 0,
    'D': 1,
    'L': 2,
    'U': 3
}
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
ROW, COL = 5, 5


def solution(dirs):
    vis_history = set()
    x, y = 0, 0
    for d in dirs:
        nx, ny = x + dx[cmd[d]], y + dy[cmd[d]]
        if nx < -ROW or nx > ROW or ny > COL or ny < -COL:
            continue
        vis_history.add(((x, y), (nx, ny)) if (x, y) < (nx, ny) else ((nx, ny), (x, y)))
        x, y = nx, ny
    return len(vis_history)
