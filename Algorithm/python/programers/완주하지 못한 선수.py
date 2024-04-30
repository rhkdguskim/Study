# https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3
from collections import defaultdict
def solution(participant, completion):
    temp = defaultdict(int)
    for p in participant:
        temp[p] += 1
    
    for c in completion:
        temp[c] -= 1
    
    for key in temp.keys():
        if temp[key]:
            return key