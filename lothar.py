def calculate(x1, y1, x2, y2):
    return (y1 + y2) * (x2 - x1) / 2  # 사다리꼴 공식

def solution(k, ranges):
    answer = []

    # 1. 우박수열 그래프 만들기
    graph = [(0, k)]
    idx = 1
    while k != 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        graph.append((idx, k))
        idx += 1

    n = len(graph) - 1  # 최대 x좌표

    # 2. 주어진 ranges 각각 처리
    for a, b in ranges:
        b = n + b  # 뒤에서 b만큼
        if a > b:
            answer.append(-1.0)
            continue

        total = 0
        for i in range(a, b):
            x1, y1 = graph[i]
            x2, y2 = graph[i + 1]
            total += calculate(x1, y1, x2, y2)

        answer.append(total)

    return answer
