# https://school.programmers.co.kr/learn/courses/30/lessons/12980
from collections import deque

def solution(n):
    queue = deque()
    queue.append((n, 0))
    vistied = [False]

    while queue:
        cur, cost = queue.popleft()

        if cur == 0:
            return cost

        if cur % 2 == 0:
            queue.append((cur//2, cost))
        else:
            queue.append((cur-1, cost + 1))

    return -1