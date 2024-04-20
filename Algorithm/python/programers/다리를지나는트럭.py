# https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3
from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    current_cnt = 0
    current_weight = 0
    answer = 0
    
    q = deque()
    
    for _ in range(bridge_length):
        q.append(0)
        
    i = 0
    while len(truck_weights) > i:
        truck = q.pop()
        if truck > 0:
            current_cnt -= 1
            current_weight -= truck
            
        current_truck = truck_weights[i]
        # 트럭이 다리에 올라갈 수 있다면
        if weight >= current_truck + current_weight and bridge_length >= current_cnt + 1:
            current_cnt += 1
            current_weight += current_truck
            q.appendleft(current_truck)
        else:
            q.appendleft(0)
            i -= 1

        i += 1
        answer += 1
        
    while q:
        q.pop()
        answer += 1
        
    return answer