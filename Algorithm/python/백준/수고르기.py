# https://www.acmicpc.net/problem/2230
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
    
A.sort()

min_value = sys.maxsize

for i in range(N):
    start = i + 1
    end = N - 1
    while end >= start:
        mid = (start + end) // 2
        cost = A[mid] - A[i]
        if cost >= M:
            min_value = min(min_value, cost)
            end = mid - 1
        else:
            start = mid + 1
            
print(min_value)