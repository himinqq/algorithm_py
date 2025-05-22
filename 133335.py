from collections import deque

truckN, bridgeW, maxL = map(int,input().split())

truckWeight = list(map(int,input().split()))

# 모든 트럭들이 다리를 건너는 최단시간
# 트럭이 다리 빠져나가려면 다리 길이만큼 시간 걸린다
# 한번에 다리 건널 수 있는 트럭 묶음 * 다리길이

bride = deque([0]*bridgeW)
time = 0
cur_weight = 0
i = 0

while i < truckN:
    time += 1 #루프 돌때마다 시간 증가
    out = bride.popleft()
    cur_weight -= out

    if cur_weight + truckWeight[i] <= maxL:
        bride.append(truckWeight[i])
        cur_weight += truckWeight[i]
        i += 1 # 트럭 건넜으면 다음 트럭 시도
    else:
        bride.append(0) # 트럭 못 들어오고 시간만 흐름

time += bridgeW
print(time)