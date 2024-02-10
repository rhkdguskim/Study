# https://www.acmicpc.net/problem/13904
import sys
import heapq

input = sys.stdin.readline
N = int(input())

works = []
for _ in range(N):
    day, cost = map(int, input().split())
    works.append((day, cost))

works.sort()

queue = []
for day, cost in works:
    heapq.heappush(queue, (cost))
    
    while len(queue) > day:
        heapq.heappop(queue)
        
print(sum(queue))

    