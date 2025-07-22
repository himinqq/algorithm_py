def solution(m, musicinfos):
    def normalize(s):
        return s.replace("C#", "c").replace("D#", "d").replace("F#", "f") \
            .replace("G#", "g").replace("A#", "a").replace("B#", "b")

    m = normalize(m)
    matched = []

    def calculate_time(s, e):
        sh, sm = map(int, s.split(":"))
        eh, em = map(int, e.split(":"))
        return (eh - sh) * 60 + (em - sm)

    def make_melody(melody, time):
        melody = normalize(melody)
        return ''.join(melody[i % len(melody)] for i in range(time))

    for info in musicinfos:
        start, end, name, melody = info.split(',')
        play_time = calculate_time(start, end)
        full_melody = make_melody(melody, play_time)
        if m in full_melody:
            matched.append((play_time, name))

    if not matched:
        return "(None)"
    matched.sort(key=lambda x: -x[0])  # 재생시간 긴 순서대로 정렬

    return matched[0][1]
