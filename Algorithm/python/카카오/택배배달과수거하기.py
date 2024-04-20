# https://school.programmers.co.kr/learn/courses/30/lessons/150369
# 그리디와 탐색문제로 접근한다.

# stack 자료구조를 이용하여 문제를 해결한다.
# pickups와, deliveries를 stack 자료구조를 이용하여 빼낸다. O(50*100,000)
# pickups[-1]과 deliveres[-1] 중에 더 큰값이 트럭이 이동해야할 거리이다. ( 거리 * 2는 해당 트럭이 이동해야할 거리)
# pickups를 cap 만큼 모두 빼낸다.
# deliveres를 cap 만큼 모두 빼낸다. 

def solution(cap, n, deliveries, pickups):
    s_deliveries = []
    s_pickups = []
    for i in range(n):
        if deliveries[i]:
            for _ in range(deliveries[i]):
                s_deliveries.append(i+1)
                
        if pickups[i]:
            for _ in range(pickups[i]):
                s_pickups.append(i+1)
    
    answer = 0
    while s_deliveries or s_pickups:
        # 재활용상자와 배달상자가 모두 있는경우
        move_pos = 0
        if s_deliveries and s_pickups:
            move_pos = max(s_deliveries[-1], s_pickups[-1])
        # 배달상자만 있는경우
        elif s_deliveries:
            move_pos = s_deliveries[-1]
        # 픽업상자만 있는경우
        else:
            move_pos = s_pickups[-1]
            
        for _ in range(cap):
            if s_deliveries:
                s_deliveries.pop()
                
            if s_pickups:
                s_pickups.pop()
            
        #트럭이 이동해야할 거리
        answer += move_pos * 2
        
    return answer

cap = 2
n = 7
deliveries = [1, 0, 2, 0, 1, 0, 2]
pickups = [0, 2, 0, 1, 0, 2, 0]
print(solution(cap, n, deliveries, pickups))