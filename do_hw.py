def convert(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m


def solution(plans):
    plans = [[name, convert(start), int(time)] for name, start, time in plans]
    plans.sort(key=lambda x: x[1])

    finish = []
    remain = []
    for i in range(len(plans) - 1):
        name, start, duration = plans[i]
        next_start = plans[i + 1][1]
        end_time = start + duration
        if end_time <= next_start:  # 다음 과제 시작 전에 끝나면
            finish.append(name)  # 완료된 과제에 저장
            left_time = next_start - end_time  # 남은 시간 계산
            while remain and left_time > 0:
                last_name, last_remain = remain.pop()  # 가장 최근에 멈췄던 과제 수행
                if last_remain <= left_time:  # 남은 시간 내에 수행할 수 있으면
                    left_time -= last_remain  # 남은 시간 갱신하고 완료된 과제에 저장
                    finish.append(last_name)
                else:
                    remain.append((last_name, last_remain - left_time))  # 남은 시간만큼 수행하고 remain에 다시 저장
                    break
        else:  # 시간 안에 못끝내면 remain에 저장하고 새로운 과제 우선 시작
            remain.append((name, duration - (next_start - start)))

    finish.append(plans[-1][0])

    while remain:
        name, _ = remain.pop()
        finish.append(name)
    return finish
# 진행중인 과제 있으면 멈추고 새로운 과제 시작
# 진행중인 과제 끝내고 멈춘과제 있으면, 그 과제 이어서 진행
# 과제 끝냈는데 새로 시작해야 하는 과제와 멈춰둔과제 둘다있으면 새로 해야되는것부터
# 멈춰둔거 여러개면 최근에 멈춘것부터 (시간이 큰것부터)
# 과제 끝낸 순서대로 이름 배열에 담아 리턴
