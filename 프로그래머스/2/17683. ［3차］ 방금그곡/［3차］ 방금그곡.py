def str_to_time(s):
    return int(s[:2]) * 60 + int(s[3:])

def replace_sharp(s):
    return s.replace('C#', 'H').replace('D#', 'I').replace('F#', 'J').replace('G#', 'K').replace('A#', 'L')

def solution(m, musicinfos):
    answer = []

    m = replace_sharp(m)
    for info in musicinfos:
        start, end, name, music = info.split(',')
        time = str_to_time(end) - str_to_time(start)
        music = replace_sharp(music)
        music_len = len(music)
        
        if music_len < time:
            music += music * (time // music_len) + music[:(time % music_len)]
        else:
            music = music[:time]
            
        if m in music:
            answer.append((time, name))

    if not answer:
        return '(None)'
    return sorted(answer, key=lambda x: (-x[0]))[0][1]
