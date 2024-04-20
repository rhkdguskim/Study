# https://www.acmicpc.net/problem/1966
from collections import deque

T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    newarr = deque()
    for i in range(N):
        newarr.append([arr[i], i])
    
    counter = 0
    while newarr:
        cost = max(newarr)[0]
        value, idx = newarr.popleft()
        if cost > value:
            newarr.append([value, idx])
        else:
            counter += 1
            if idx == M:
                print(counter)
    
    