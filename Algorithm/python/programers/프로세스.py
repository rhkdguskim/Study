import heapq
from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque()
    p_q = []
    
    for i, process in enumerate(priorities):
        queue.append((i, process))
        heapq.heappush(p_q, -process)
    
    while queue:
        idx, process = queue.popleft()
        
        max_process = p_q[0] * -1
        if max_process > process:
            queue.append((idx, process))
        else:
            answer += 1
            if location == idx:
                break
            
            heapq.heappop(p_q)
        
    return answer