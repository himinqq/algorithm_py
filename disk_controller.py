import heapq

def solution(jobs):
    jobs.sort()  # 요청 시각 기준 정렬
    n = len(jobs)
    heap = [] # 대기 중인 작업 담는 최소 힙 (소요시간 짧은순)
    time = 0 # 현재 시각
    next_job = 0 # 다음 작업의 인덱스
    total = 0 # 모든 작업의 반환시간 합 (반환시간 = 종료시각 - 요청시각)

    # 모든 작업 처리할 때 까지 반복
    while next_job < n or heap:
        # 현재 시간까지 요청된 작업 힙에 넣기
        while next_job < n and jobs[next_job][0] <= time:
            req, dur = jobs[next_job]
            heapq.heappush(heap, (dur, req)) # (소요시간, 요청시각)으로 넣어 최소 힙 유지
            next_job += 1 # 다음 작업으로 이동

        if heap: # 대기 중인 작업 있으면
            dur, req = heapq.heappop(heap) # 소요 시간이 가장 짧은 작업 선택
            time += dur # 작업 처리 (현재 시간을 소요 시간만큼 증가 시킴)
            total += time - req
        else: # 힙이 비었다면 아직 작업 요청되지 않은 상태
            time = jobs[next_job][0]  # 다음 작업 요청 시간으로 점프

    return total // n # 평균 반환 시간 리턴
