import heapq


def solution(n, k, enemy):
    q = []
    total = 0
    answer = 0
    for e in enemy:
        heapq.heappush(q,-e) # 최대 힙으로 사용하기 위해 음수 저장
        total += e # 일단 병사로 막기
        if total > n: # 병사 수 초과 시
            if k == 0: break # 무적권도 없으면 종료
            total += heapq.heappop(q) # 음수 pop → 다시 total에 더해서 상쇄
            k -= 1 # 무적권 사용
        answer += 1 # 1 라운드 통과
    return answer