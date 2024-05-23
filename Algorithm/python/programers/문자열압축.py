# https://school.programmers.co.kr/learn/courses/30/lessons/60057

# 모든 경우의 수를 다 탐색해본다.
def solution(s):
    length = len(s)
    for n in range(1, length + 1):
        idx = 0
        char = {}
        while length >= idx:
            if length >= idx+n+n:
                print(s[idx:idx+n], s[idx+n:idx+n+n])
                if s[idx:idx+n] == s[idx+n:idx+n+n]:
                    idx += n + n
                    continue
            
            idx += 1
            
    answer = 0
    return answer

solution("aabbaccc")