def solution(targets):
    targets.sort(key= lambda x: x[1])
    cnt, end = 0, 0
    for s,e in targets:
        if s >= end: # 이전에 요격한 미사일 끝점보다 크거나 같으면
            cnt += 1 # 요격 미사일 발사 (범위 겹치지 않음)
            end = e # 끝점 갱신

    # 모든 폭격 미사일을 요격하기 위해 필요한 요격 미사일 수의 최솟값
    return cnt