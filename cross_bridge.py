def solution(stones, k):
    # 건널 수 있는 사람 수 기준으로 이분탐색
    # mid 명 건널 수 있는지 확인하기 (연속 k 칸 이상이면 실패)
    # 한 디딤돌의 내구도보다 많은 사람은 절대 건널 수 없음

    start, end = 1, max(stones)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0  # 0 이하인 돌의 개수 세기 (연속으로 k개 이상이면 mid 명 건널 수 없음)
        for stone in stones:
            if stone - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:  # mid 값 줄이기
            end = mid - 1
        else:
            start = mid + 1

    return start
