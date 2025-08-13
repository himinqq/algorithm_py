from collections import deque


def solution(begin, target, words):

    # 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지
    def bfs(beg,tar):
        q = deque()
        q.append((beg,0))
        while q:
            now, cnt = q.popleft()
            if now == tar:
                return cnt
            for w in words:
                diff = 0
                for i in range(len(w)):
                    if w[i] != now[i]:
                        diff += 1
                if diff == 1:
                    q.append((w,cnt+1))

    if target not in words:
        return 0
    else:
        return bfs(begin,target)
