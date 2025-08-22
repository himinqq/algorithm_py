N, M, T = map(int, input().split())
dart = [list(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    x, d, k = map(int, input().split())
    k %= M

    # x의 배수 원판만 회전
    for i in range(N):
        if (i + 1) % x != 0:
            continue
        if d == 0:  # 시계
            dart[i] = dart[i][-k:] + dart[i][:-k]
        else:       # 반시계
            dart[i] = dart[i][k:] + dart[i][:k]

    # 인접 수 찾기
    remove_list = set()
    for i in range(N):
        for j in range(M):
            if dart[i][j] == 0:
                continue
            # 같은 원판
            if dart[i][j] == dart[i][(j+1)%M]:
                remove_list.add((i, j))
                remove_list.add((i, (j+1)%M))
            # 위 아래 원판
            if i > 0 and dart[i][j] == dart[i-1][j]:
                remove_list.add((i, j))
                remove_list.add((i-1, j))
            if i < N-1 and dart[i][j] == dart[i+1][j]:
                remove_list.add((i, j))
                remove_list.add((i+1, j))

    # 인접 수 제거
    if remove_list:
        for i, j in remove_list:
            dart[i][j] = 0
    else:
        # 평균 계산 (0 제외)
        total = 0
        count = 0
        for i in range(N):
            for j in range(M):
                if dart[i][j] != 0:
                    total += dart[i][j]
                    count += 1
        if count == 0:
            continue
        avg = total / count
        for i in range(N):
            for j in range(M):
                if dart[i][j] == 0:
                    continue
                if dart[i][j] > avg:
                    dart[i][j] -= 1
                elif dart[i][j] < avg:
                    dart[i][j] += 1

# 최종 합 출력
result = sum(sum(row) for row in dart)
print(result)
