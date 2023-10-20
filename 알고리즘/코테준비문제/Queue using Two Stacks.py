# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem?isFullScreen=true
import sys
from collections import deque

input = sys.stdin.readline

q = int(input())
queue = deque()
for _ in range(q):
    temp = list(map(int, input().split()))
    if temp[0] == 1: # enqueue
        queue.append(temp[1])
    if temp[0] == 2: # dequeue
        queue.popleft()
    if temp[0] == 3: # print front queue
        print(queue[0])

