def solution(play_time, adv_time, logs):
    
    def time_to_sec(time : str):
        h, m, s = map(int, time.split(":"))
        return h*3600 + m*60 + s
    
    def sec_to_time(sec : int):
        return f'{sec//3600:02d}:{sec%3600//60:02d}:{sec%60:02d}'
    
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    p_s = [0] * (play_time + 1)
    r_c = [0] * (play_time + 1)
    
    for log in logs:
        s, e = log.split("-")
        s = time_to_sec(s)
        e = time_to_sec(e)
        r_c[s] += 1
        r_c[e] -= 1
    
    for i in range(1, play_time + 1):
        r_c[i] += r_c[i-1]
        p_s[i] = p_s[i-1] + r_c[i]
    
    answer = max((p_s[start_time + adv_time - 1] - (p_s[start_time-1] if start_time - 1 > 0 else 0), -start_time) 
                 for start_time in range(play_time - adv_time +1))
    
    return sec_to_time(-answer[1])