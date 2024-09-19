# https://school.programmers.co.kr/learn/courses/30/lessons/214288
from collections import deque
import heapq

def solution(k, n, reqs):
    # 배정하는 방법을 완전탐색한다.
    mentors = [1 for _ in range(k)]
    n -= k
    
    def dfs(n):
        if n == 0:
            total_delayed = 0
            for m in range(k):
                mentors_cnt = mentors[m]
                q = deque(filter(lambda x:x[2] == m+1, reqs))
                schdule = [0 for _ in range(mentors_cnt)]
                heapq.heapify(schdule)
                
                while q:
                    # 요청시간, 상담시간
                    a, b, _ = q.popleft()
                    
                    time = heapq.heappop(schdule)
                    if time == 0:
                        heapq.heappush(schdule, a+b)
                        continue
                    
                    delayed_time = abs(time - a)
                    
                    # 기다림 없이 바로 업데이트
                    if delayed_time == 0:
                        heapq.heappush(schdule, time + b)
                    # 기다린시간 + 요청시간
                    else:
                        total_delayed += delayed_time
                        heapq.heappush(schdule, time + b)
            
            
            return total_delayed

        min_v = int(1e9)
        for i in range(k):            
            mentors[i] += 1
            min_v = min(dfs(n-1), min_v)
            mentors[i] -= 1
            
        return min_v
    
    
    answer = dfs(n)
    return answer