def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    a_idx = 0
    
    for b in B:
        if b > A[a_idx]:
            a_idx += 1
            answer += 1
            
    return answer

