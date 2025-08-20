def solution(n, stations, w):
    answer = 0
    start = 1
    cover = 1 + w * 2
    idx = 0
    stations.sort()

    while start <= n:
        # 기존 기지국 커버 안에 들어오면 커버 끝으로 점프
        if idx < len(stations) and start >=  stations[idx] - w:
            start = stations[idx] + w + 1
            idx += 1
        else: # 아니면 새 기지국 설치 후 cover 만큼 점프
            answer += 1
            start += cover
    return answer
