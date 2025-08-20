def solution(routes):
    answer = 0
    routes.sort(key= lambda x:x[1])
    prev_end = routes[0][1]
    for cur_s, cur_e in routes:
        if prev_end <= cur_s:
            answer += 1
            prev_end = cur_e
    return answer