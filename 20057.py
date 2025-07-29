# 토네이도가 (s_x,s_y) 위치에 도착하면, 그 칸의 모래를 해당 방향 기준 비율대로 뿌림
def recount(s_x, s_y, direction):
    global ans

    if s_y < 0:
        return

    # 3. a, out_sand
    total = 0  # a 구하기 위한 변수
    for dx, dy, z in direction:
        nx = s_x + dx
        ny = s_y + dy
        if z == 0:  # a(나머지)
            new_sand = sand[s_x][s_y] - total # 원래 모래량 - total = 남은 모래량 > 이걸 a 위치에 몰아서 보냄
        else:  # 비율로 퍼트리기
            new_sand = int(sand[s_x][s_y] * z) #소수점 버림 (int 사용), total에 누적
            total += new_sand

        if 0 <= nx < N and 0 <= ny < N:  # 모래가 격자 내부이면
            sand[nx][ny] += new_sand # 해당 위치에 모래 누적
        else:  # 범위 밖이면 ans 카운트
            ans += new_sand


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

# 2. 방향별 모래 비율 위치 // (x, y, 비율) 형태로 모래 퍼질 좌표 정의
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
        (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left] # 좌우 대칭
down = [(-y, x, z) for x, y, z in left] #90도 시계 방향 회전
up = [(y, x, z) for x, y, z in left] # 90도 반시계 방향 회전

s_x, s_y = N // 2, N // 2 # 격자 가운데서 시작
ans = 0
# 토네이도 회전 방향 왼→아래→오른→위
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 1.토네이도 회전 방향(y위치)
dict = {0: left, 1: down, 2: right, 3: up}
time = 0 #  현재 방향으로 몇 칸 이동할지
for i in range(2 * N - 1):
    # 몫: i//4(타임+1), 나머지:i%4(방향)
    d = i % 4
    if d == 0 or d == 2:  # 다음 회차(d==0) left 이거나 right(d==2) 이면 한번 더
        time += 1 # 두 방향마다 이동 거리 증가
    for _ in range(time): # 현재 방향d로 time 만큼 이동
        n_x = s_x + dx[d]
        n_y = s_y + dy[d]
        recount(n_x, n_y, dict[d])  # y좌표, 방향
        s_x, s_y = n_x, n_y

print(ans)