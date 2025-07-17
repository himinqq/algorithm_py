def solution(players, m, k):
    server = [0] * 24
    answer = 0

    for time in range(24):
        need = players[time] // m  # 필요한 서버의 수

        if need > server[time]:  # 필요한 서버의 수가 증설된 서버의 수보다 크면
            to_add = need - server[time]  # 증설 횟수
            answer += to_add

            for j in range(time, min(time + k, 24)):
                server[j] += to_add

    return answer