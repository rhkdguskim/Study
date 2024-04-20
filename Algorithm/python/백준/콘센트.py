#https://www.acmicpc.net/problem/23843
import heapq, sys
input = sys.stdin.readline
N, M = map(int, input().split())
devices = list(map(int, input().split()))
devices.sort(key=lambda x:-x)

queue = []
ans = 0
for device in devices:
    if M > len(queue):
        heapq.heappush(queue, device)
    else:
        time = queue[0]
        ans += time
        
        for i in range(len(queue)):
            queue[i] -= time
        
        while queue and queue[0] == 0:
            heapq.heappop(queue)
            
        heapq.heappush(queue, device)
    
while queue:
    time = queue[0]
    ans += time
    for i in range(len(queue)):
        queue[i] -= time
    
    while queue and queue[0] == 0:
        heapq.heappop(queue)
            
print(ans)