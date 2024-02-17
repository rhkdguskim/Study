# https://www.acmicpc.net/problem/1826
import sys
import heapq
input = sys.stdin.readline


N = int(input())

oil_station = []

for _ in range(N):
    a, b = map(int, input().split())
    oil_station.append((a, b))
    
oil_station.sort(key=lambda x:(x[0], -x[1]))

queue = []
cnt = 0
L, P = map(int, input().split())
oil_station.append((L, 0))

for next, oil in oil_station:
    if P >= L:
        break
    
    while next > P and queue:
        P += -heapq.heappop(queue)
        cnt += 1
    
    if next > P:
        break
    
    heapq.heappush(queue, -oil)


print(cnt if P >= L else -1)
        
        


