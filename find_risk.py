from collections import Counter


def solution(points, routes):
    answer = 0

    # (시간, x, y) 좌표에 몇 대의 로봇이 있는지 기록
    collision_counter = Counter()

    for route in routes:
        time = 0
        # 첫 번째 포인트 처리
        curr_x, curr_y = points[route[0] - 1]
        collision_counter[(time, curr_x, curr_y)] += 1

        for i in range(len(route) - 1):
            start_x, start_y = points[route[i] - 1]
            end_x, end_y = points[route[i + 1] - 1]
            # X좌표가 다르면 X 이동 먼저
            while start_x != end_x:
                if start_x < end_x:
                    start_x += 1
                else:
                    start_x -= 1
                time += 1
                collision_counter[(time, start_x, start_y)] += 1

            # Y좌표가 다르면 Y 이동
            while start_y != end_y:
                if start_y < end_y:
                    start_y += 1
                else:
                    start_y -= 1
                time += 1
                collision_counter[(time, start_x, start_y)] += 1

    # 충돌 횟수 계산
    for count in collision_counter.values():
        # 한 시점에 한 지점에 2대 이상 모이면 위험 상황
        if count >= 2:
            answer += 1

    return answer
