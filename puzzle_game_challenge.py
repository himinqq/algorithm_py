def solution(diffs, times, limit):
    def total_time(level): # 퍼즐을 푸는 데 걸리는 총 시간
        total = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            cur_time = times[i]
            prev_time = times[i - 1] if i > 0 else 0

            if level >= diff:
                total += cur_time
            else:
                wrong = diff - level
                total += wrong * (cur_time + prev_time) + cur_time

        return total

    left = 1
    right = max(diffs)
    answer = right
    while left <= right:
        mid = (left+right) // 2
        if total_time(mid) <= limit: # limit 보다 작거나 같으면
            answer = mid # 정답 후보에 기록하고
            right = mid - 1 # 더 작은값 탐색
        else:
            left = mid + 1 #  # 제한 시간을 초과하므로 더 높은 숙련도 필요

    return answer

