# https://www.acmicpc.net/problem/12851
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
vistied = [-1] * 100001

queue = deque()
queue.append((N))
vistied[N] = 0
ans = 0

while queue:
    cur = queue.popleft()
    
    if cur == K:
        ans += 1
        continue
    
    for next in (cur*2, cur + 1, cur - 1):
        if 100001 > next >=0 and (vistied[next] == vistied[cur] + 1 or vistied[next] == -1):
            vistied[next] = vistied[cur] + 1
            queue.append((next))    
            
print(vistied[K])
print(ans)
        