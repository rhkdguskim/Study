# https://school.programmers.co.kr/learn/courses/30/lessons/12987

# 원소의 길이가 10만임으로, nlogn 알고리즘으로 풀어야한다.
# 삭제 -> n # 찾기 log n
import bisect

def solution(A, B):
    B.sort()
    answer = 0
    
    for a in A:
        idx = bisect.bisect_right(B, a)
        if idx == len(B):
            continue
        
        if B[idx] >= a:
            answer += 1
            B.pop(idx)
            
    return answer

