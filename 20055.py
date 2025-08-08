N, K = map(int, input().split())
durability = list(map(int, input().split()))
robots = [0] * (2 * N)  # 로봇 위치: 0-없음, 1-있음

step = 0

while True:
    step += 1

    # 1. 벨트와 로봇 한 칸 회전
    durability = [durability[-1]] + durability[:-1]
    robots = [robots[-1]] + robots[:-1]
    robots[N-1] = 0  # 로봇 내리는 위치는 비워줌

    # 2. 로봇 이동
    for i in range(N-2, -1, -1):  # N-2부터 0까지 역순으로
        if robots[i] == 1 and robots[i+1] == 0 and durability[i+1] > 0:
            robots[i] = 0
            robots[i+1] = 1
            durability[i+1] -= 1
    robots[N-1] = 0  # 내리는 위치 로봇 내림

    # 3. 올리는 위치에 로봇 올림
    if durability[0] > 0 and robots[0] == 0:
        robots[0] = 1
        durability[0] -= 1

    # 4. 내구도 0인 칸 개수 체크
    if durability.count(0) >= K:
        break

print(step)
