# https://www.acmicpc.net/problem/1655
from collections import deque
from bisect import bisect_left

N = int(input())
queue = deque()
for _ in range(N):
    num = int(input())
    if len(queue) > 1:
        if queue[0] > num:
            queue.appendleft(num)
        elif queue[-1] > num:
            idx = bisect_left(queue, num)
            queue.insert(idx, num)
        else:
            queue.append(num)
    else:
        queue.append(num)
        
    #print(queue)
    if len(queue) == 1:
        print(queue[-1])
    else:
        if len(queue) % 2 == 0: # 짝수일때
            n = len(queue) // 2
            print(min(queue[n], queue[n-1]))
        else: # 홀수일때
            n = len(queue) // 2
            print(queue[n])