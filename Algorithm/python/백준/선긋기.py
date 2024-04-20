# https://www.acmicpc.net/problem/2170
import sys
import heapq

input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))
    
arr.sort()

queue = []

heapq.heappush(queue, (arr[0][0], arr[0][1]))

for i in range(1, N):
    start, end = arr[i]
    
    new_queue = []
    
    is_added = False
    while queue:
        p_start, p_end = heapq.heappop(queue)
        if p_end >= start:
            is_added = True
            p_end = max(p_end, end)
            
        heapq.heappush(new_queue, (p_start, p_end))
        
    if not is_added:
        heapq.heappush(new_queue, (start, end))
        
    queue = new_queue
    
ans = 0    
for i in range(len(queue)):
    ans += queue[i][1] - queue[i][0]
    
print(ans)