from collections import defaultdict, deque

def calculate_fee(time_list, fees):
    tmp = deque(time_list)
    total_time = 0

    while tmp:
        time_in = tmp.popleft()  # 항상 IN
        if tmp:
            time_out = tmp.popleft()  # OUT
        else:
            time_out = 23 * 60 + 59  # 출차 기록 없으면 23:59

        time = time_out - time_in
        total_time += time

    if total_time <= fees[0]:  # 기본 시간 이하면 기본 요금
        return fees[1]
    else:
        extra_time = total_time - fees[0]
        extra_fee = ((extra_time + fees[2] - 1) // fees[2]) * fees[3]  # 올림
        return fees[1] + extra_fee

def solution(fees, records):
    answer = []
    car_record = defaultdict(deque)

    for record in records:
        time, num, stamp = record.split()
        h, m = map(int, time.split(":"))
        total_min = h * 60 + m
        car_record[num].append(total_min)  # 시간만 저장

    for car in sorted(car_record.keys()):
        fee = calculate_fee(car_record[car], fees)
        answer.append(fee)

    return answer
