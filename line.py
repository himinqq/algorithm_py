from collections import deque

def facto(n):
    if n == 1:
        return 1
    return n * facto(n-1)

# 팩토리얼의 구조를 활용해, 각 자리마다 어떤 수가 올지 순서대로 결정
def solution(n, k):
    answer = []
    q = deque([i for i in range(1,n+1)])

    # 0-indexed 이므로 k-1
    while n > 1:
        fac = facto(n-1) # 현재 자리에서 가능한 경우의 수는 (n-1)!개
        num = q[(k-1)//fac]
        answer.append(num)
        q.remove(num)
        n -= 1
        k %= fac # 남은 순열 중에서 몇 번째인지 인덱스 갱신
    answer.append(q[-1])
    return answer