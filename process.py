from collections import deque

def solution(priorities, location):
    q = deque([(i,p) for i,p in enumerate(priorities)])

    idx = 0
    while q:
        cur = q.popleft()
        if any(cur[1] < other[1] for other in q):
            q.append(cur)
        else:
            idx += 1
            if cur[0] == location:
                return idx

