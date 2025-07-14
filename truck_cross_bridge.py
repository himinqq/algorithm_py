from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque(bridge_length*[0])

    time = 0
    idx = 0
    curr_weight = 0

    while idx < len(truck_weights): #모든 트럭이 다리를 올라가는 경우만 계산
        time += 1 # 1초마다 트럭이 움직이며 다리를 빠져나감
        w = bridge.popleft()
        curr_weight -= w

        truck = truck_weights[idx] #현재 확인할 트럭
        if truck+ curr_weight <= weight: #조건 만족하면
            curr_weight += truck
            bridge.append(truck)
            idx += 1

        else: #조건 만족하지 않으면 시간만 흐름
            bridge.append(0)

    time += bridge_length #마지막 트럭이 다리를 빠져나가는 시간 더해주기
    return time