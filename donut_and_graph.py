def solution(edges):
    answer = [0,0,0,0]
    n = max(max(u,v) for u,v in edges) + 1
    out_count = [0] * n
    in_count = [0] * n

    for out_c, in_c in edges:
        in_count[in_c] += 1
        out_count[out_c] += 1
    for node in range(1,n):
        i = in_count[node]
        o = out_count[node]
        if i  == 0 and o >= 2: # 생성 쟁점
            answer[0] = node
        elif i >= 1 and o == 0: # 막대 그래프
            answer[2] += 1
        elif i >= 2 and o == 2: # 도넛 그래프
            answer[3] += 1
    answer[1] = out_count[answer[0]] - answer[2] - answer[3]

    # 생성한 정점의 번호0, 도넛 모양 그래프의 수1, 막대 모양 그래프의 수2, 8자 모양 그래프3의 수를 순서대로
    return answer