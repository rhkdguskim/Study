# https://school.programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):
    # n 은 사람의수 times 는 입국심사
    times.sort()
    start = 1
    end = times[-1] * n
    answer = times[-1] * n
    while end >= start:
        mid = (start + end) // 2
        
        cnt = 0
        # 걸린시간을 계산하자.
        for t in times:
            cnt += mid // t
            
        # 입국심사 가능함 시간을 줄여보자
        if cnt >= n:
            end = mid - 1
            answer = min(mid, answer)
        # 입국심사가 불가능함 시간을 늘려 보자
        else:
            start = mid + 1    
    
    return answer
