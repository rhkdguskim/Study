# https://www.acmicpc.net/problem/2014
import sys
import bisect

input = sys.stdin.readline

K, N = map(int, input().split())

prime = list(map(int, input().split()))

queue = []

for i, p in enumerate(prime):
    queue.append(p)

cnt = 0
is_founded = False
while True:
    if is_founded:
        break
    
    for n in queue:
        for p in prime:
            idx = bisect.bisect_left(queue, n*p)
            if idx == len(queue):
                queue.append(n*p)
            else:
                if queue[idx] == n*p:
                    continue
                else:
                    queue.insert(idx, n*p)
        if len(queue) >= N:
            is_founded = True
            break
    
print(queue[N-1])
