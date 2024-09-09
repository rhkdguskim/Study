# https://school.programmers.co.kr/learn/courses/30/lessons/340213

def solution(video_len, pos, op_start, op_end, commands):
    def to_time(time : str): 
        min, sec = time.split(":")
        min = int(min)
        sec = int(sec)
        return min*60 + sec
    
    def to_time_string(time: int):
        min = time // 60
        sec = time % 60
        return "{:02d}:{:02d}".format(min, sec)

    def next(time : int):
        return min(to_time(video_len), time + 10)
    
    def prev(time : int):
        return max(0, time - 10)

    def skip_opening(time : int):
        start = to_time(op_start)
        end = to_time(op_end)
        if start <= time <= end:
            return end
        else:
            return time
    
    
    cur_time = skip_opening(to_time(pos))
    
    for op in commands:
        if op == "next":
            cur_time = next(cur_time)
        else:
            cur_time = prev(cur_time)
            
        cur_time = skip_opening(cur_time)
    
        
    answer = to_time_string(cur_time)
    return answer
    
print(solution("34:33",
               "13:00", 
               "00:55",
               "02:55", 
               ["next", "prev"]))