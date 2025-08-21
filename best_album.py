from collections import defaultdict


def solution(genres, plays):
    answer = []
    # 많이 재생된 장르 > 많이 재생된 노래 > 고유번호 낮은 순서대로 정렬
    songs = defaultdict(list)
    # 장르: [고유번호,재생횟수]
    for idx, g in enumerate(genres):
        songs[g].append([idx,plays[idx]])


    g_sort = []
    for k,v in songs.items():
        play_cnt = sum(map(lambda x:x[1],v))
        g_sort.append([k,play_cnt])
    g_sort.sort(key=lambda x:x[1],reverse=True)

    for genre,_ in g_sort:
        song_list = songs[genre]
        song_list.sort(key=lambda x:(-x[1],x[0]))
        answer.extend([num for num,cnt in song_list])

    return answer