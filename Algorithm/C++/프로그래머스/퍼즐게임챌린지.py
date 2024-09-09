# https://school.programmers.co.kr/learn/courses/30/lessons/340212

def solution(diffs, times, limit):
    def play(prev_time, diff, time, cursor):
        if diff > cursor:
            cnt = diff - cursor
            return (time + prev_time) * cnt + time
        else:
            return time
        
    def search(mid : int):
        prev_time = 0
        total = 0
        for diff, time in zip(diffs, times):
            payload = play(prev_time, diff, time, mid)
            prev_time = time
            total += payload
            
        if limit >= total:
            return True
        else:
            return False
        
    start = 1
    end = max(diffs)
    answer = 0
    while end >= start:
        mid = (start + end) // 2
        ret = search(mid)
        if ret:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
        
    return answer