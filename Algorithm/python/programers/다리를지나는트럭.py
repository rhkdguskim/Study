# https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3
from collections import deque

DUMMY_TRUCK = 0
class Bridge(object):
    def __init__(self, length, weight):
        self.max_weight = weight
        self.current_cnt = 0
        self.current_weight = 0
        self.legnth = length
        self.queue = deque()
        for _ in range(length):
            self.queue.append(DUMMY_TRUCK)

    def pop_truck(self):
        truck = self.queue.pop()
        if truck:
            self.current_cnt -= 1
            self.current_weight -= truck

    def push_truck(self, truck):
        if truck == DUMMY_TRUCK:
            self.queue.appendleft(truck)
            return True

        if self.max_weight >= self.current_weight + truck and self.legnth >= self.current_cnt + 1:
            self.current_cnt += 1
            self.current_weight += truck
            self.queue.appendleft(truck)
            return True
        else:
            return False

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = deque(w for w in truck_weights)
    answer = 0
    while trucks:
        bridge.pop_truck()
        # 트럭이 다리에 올라갈 수 있다면
        is_pushed = bridge.push_truck(trucks[0])

        if is_pushed:
            trucks.popleft()
        else:
            bridge.push_truck(DUMMY_TRUCK)

        answer += 1
        
    answer += len(bridge)
        
    return answer