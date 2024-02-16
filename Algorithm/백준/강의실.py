# https://www.acmicpc.net/problem/1374
import sys
import heapq

input = sys.stdin.readline

N = int(input())
rooms = []
for _ in range(N):
    idx, start, end = map(int, input().split())
    rooms.append((start, end))
    
rooms.sort(key=lambda x:(x[0], x[1]))

queue = []
for start, end in rooms:
    if queue and start >= queue[0]:
        heapq.heappop(queue)
        
    heapq.heappush(queue, end)

print(len(queue))
