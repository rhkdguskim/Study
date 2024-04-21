# https://school.programmers.co.kr/learn/courses/30/lessons/42586
import math

def solution(progresses, speeds):
    days = []
    for p, s in zip(progresses, speeds):
        day = math.ceil((100-p)/s)
        if not days:
            days.append([day, 1])
        else:
            if days[-1][0] >= day:
                days[-1][1] += 1
            else:
                days.append([day, 1])

    _, d = zip(*days)
    
    return d