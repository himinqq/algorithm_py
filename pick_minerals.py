# 그리디
# 가장 최악의 피로도 기준으로 계산해놓고, 좋은 곡괭이부터 그 피로도 높은 묶음에 할당하면 전체 피로도 총합이 최소
def solution(picks, minerals):
    answer = 0
    tools_info = {
        0: {"diamond": 1, "iron": 1, "stone": 1},     # 다이아곡괭이
        1: {"diamond": 5, "iron": 1, "stone": 1},     # 철곡괭이
        2: {"diamond": 25, "iron": 5, "stone": 1}     # 돌곡괭이
    }

    # 1. 광물 5개씩 묶기
    chunks = []
    for i in range(0, len(minerals), 5):
        chunk = minerals[i:i + 5]
        chunks.append(chunk)

    # 2. 곡괭이 수만큼 자르기
    total_picks = sum(picks)
    chunks = chunks[:total_picks]  # 곡괭이 개수 이상 캐지 못하므로

    # 3. 각 묶음 "피로도" 많이 드는 기준 정렬 (돌곡괭이로 캤을 때 가장 높음)

    def chunk_weight(chunk):  # 한 묶음에 포함된 광물들을 돌 곡괭이로 캤을 때 누적 피로도를 계산
        return sum(tools_info[2][m] for m in chunk)

    chunks.sort(key=chunk_weight, reverse=True) # 각 묶음을 돌 곡괭이 기준으로 정렬해서, 높은 피로도 순

    # 4. 가장 좋은 곡괭이부터 할당
    #  성능이 좋은 곡괭이(다이아몬드 곡괭이)는 피로도가 많이 드는 묶음에 써야 효율적
    tool_order = []
    for i, count in enumerate(picks):
        tool_order += [i] * count

    for tool, chunk in zip(tool_order, chunks):
        for m in chunk:
            answer += tools_info[tool][m]

    return answer
