# https://www.acmicpc.net/problem/1781
import sys
import heapq

input = sys.stdin.readline

N = int(input())

problem = []
for _ in range(N):
     a, b = map(int, input().split())
     problem.append((a, b)) # 데드라인, 컵라면수

problem.sort(key=lambda x:x[0])

queue = []
for deadline, score in problem:
    heapq.heappush(queue, score)
    
    if len(queue) > deadline:
        heapq.heappop(queue)

print(sum(queue))
        
    