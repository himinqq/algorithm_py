import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# 초기 상태
visited = [False] * N
result = float('inf')

# 조건 판단 함수
def is_complete_team(depth):
    return depth == N // 2

# 상태 갱신 함수
def calculate_team_diff():
    start_team, link_team = 0, 0
    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:
                start_team += S[i][j]
            elif not visited[i] and not visited[j]:
                link_team += S[i][j]
    return abs(start_team - link_team)

# 시뮬 루프 (백트래킹)
def dfs(depth, idx):
    global result

    if is_complete_team(depth):
        diff = calculate_team_diff()
        result = min(result, diff)
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False  # 백트래킹

# 시작
dfs(0, 0)
print(result)
