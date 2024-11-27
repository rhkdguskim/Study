import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())

start = 1
q = []
while N > 1:
    if N % 2 != 0:
        heapq.heappush(q, start)
    N //= 2
    start *= 2
    
heapq.heappush(q, start)

cost = 0
while len(q) > K:
    v = heapq.heappop(q)
    if q[0] == v:
        heapq.heappop(q)
        heapq.heappush(q, v*2)
    else:
        cost += v
        heapq.heappush(q, v*2)
print(cost)
