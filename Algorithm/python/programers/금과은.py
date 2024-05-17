# https://school.programmers.co.kr/learn/courses/30/lessons/86053

# 시간을 기준으로 이분탐색한다.
import sys

def solution(a, b, g, s, w, t):
    # 도시의 개수
    n = len(g)
    start = 1
    end = sys.maxsize
    answer = sys.maxsize
    
    while end >= start:
        mid = (start+end) // 2
        total = 0
        g_total = 0
        s_total = 0
        
        for i in range(n):
            # 해당시간에 옮길 수 있는 횟수
            cnt = mid // (t[i]*2)
            
            # 편도로 갔다와야하는경우의 수 추가
            if mid % (t[i]*2) >= t[i]:
                cnt += 1
            
            # 시간내에 옮길 수 있는 최대 무게
            tmp = w[i] * cnt
            
            total += min(tmp, g[i] + s[i])
            g_total += min(tmp, g[i])
            s_total += min(tmp, s[i])
        
        # 옮길 수 있는지 확인 없다면 시간을 늘린다 그렇지 않다면 시간을 줄여본다.
        if total >= a+b and g_total >= a and s_total >= b:
            answer = min(mid, answer)
            end = mid - 1
        else:
            start = mid + 1
    
    return answer