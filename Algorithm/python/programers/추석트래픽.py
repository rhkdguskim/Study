# https://school.programmers.co.kr/learn/courses/30/lessons/17676?language=python3

def solution(lines):
    def time_to_millisec(time: str):
        h, m, s = map(float, time.split(':'))
        return (float(h) * 3600 + float(m) * 60 + float(s))

    def to_start_end(line: str):
        date, time, duration = line.split()
        duration = float(duration[:-1])
        end_time = time_to_millisec(time)
        start_time = end_time - duration + 0.001
        return (start_time, end_time)
    
    intervals = list(map(to_start_end, lines))
    max_count = 0
    
    for i in range(len(intervals)):
        start_window = intervals[i][1]
        end_window = start_window + 1
        count = 0
        for start, end in intervals:
            if start < end_window and end >= start_window:
                count += 1
        max_count = max(max_count, count)

    return max_count