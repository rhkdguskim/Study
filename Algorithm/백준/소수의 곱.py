# https://www.acmicpc.net/problem/2014
import sys
import heapq

input = sys.stdin.readline

K, N = map(int, input().split())

prime = list(map(int, input().split()))

queue = []

for p in prime:
    heapq.heappush(queue, p)
    
for _ in range(N):
    num = heapq.heappop(queue)
    
    for i in range(K):
        data = num * prime[i]
        heapq.heappush(queue, data)
        
        if num % prime[i] == 0:
            break

print(num)