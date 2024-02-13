# https://www.acmicpc.net/problem/1699
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

queue = deque()
squre_number = []
vistied = [False for _ in range(N+1)]
vistied[1] = True
queue.append((1, 1))
squre_number.append(1)

i = 1
cnt = 1
while N >= i:
    cnt += 1
    i = cnt**2
    if N >= i:
        queue.append((i, 1))
        squre_number.append(i)
        vistied[i] = True

while queue:
    num, cost = queue.popleft()
    if num == N:
        print(cost)
        break
    
    for n in squre_number:
        if N >= n + num and not vistied[n+num]:
            vistied[n+num] = True
            queue.append((n+num, cost + 1))
