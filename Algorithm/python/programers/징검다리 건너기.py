# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    start = 0
    end = 200000001
    answer = -1
    n = len(stones)
    while end >= start:
        mid = (start + end) // 2
        cnt = 0
        can_go = True
        for i in range(n):
            # 해당돌을 건널 수 없음
            if mid > stones[i]:
                cnt += 1
            else:
                cnt = 0
            
            if cnt >= k:
                can_go = False
                break
            
        if can_go:
            answer = max(mid, answer)
            start = mid + 1
        else:
            end = mid - 1
    
    return answer