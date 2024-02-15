# https://www.acmicpc.net/problem/13334
import sys
import heapq
input = sys.stdin.readline

n = int(input())

road = []
for _ in range(n):
    road.append((sorted(list(map(int, input().split())))))
    
road.sort(key=lambda x:(x[1], x[0]))

d = int(input())

ans = 0
queue = []
for s, e in road:
    heapq.heappush(queue ,s)
    
    line_start = e - d
    while queue and line_start > queue[0]:
        heapq.heappop(queue)
    
    ans = max(ans, len(queue))

print(ans)