import heapq


def solution(operations):
    answer = []
    q = []
    for op in operations:
        cmd, num = op.split()
        if cmd == 'I':
            heapq.heappush(q, int(num))
        elif cmd == 'D' and q:
            if int(num) == -1:
                heapq.heappop(q)
            else:
                max_value = max(q)
                q.remove(max_value)

    q.sort()
    if not q:
        return [0, 0]
    else:
        answer.append(q[-1])
        answer.append(q[0])

    return answer
