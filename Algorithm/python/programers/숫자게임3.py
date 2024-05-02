import heapq

def solution(A, B):
    A.sort()
    heapq.heapify(B)
    answer = 0
    a_idx = 0
    
    while B:
        b = heapq.heappop(B)
        if b > A[a_idx]:
            a_idx += 1
            answer += 1
            
    return answer

