# https://www.acmicpc.net/problem/11054
import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dpr = [1 for _ in range(N)]
dpl = [1 for _ in range(N)]
dpr[0] = 1
dpl[0] = 1

r = [A[0]]
for i in range(1, N):
    if  A[i] > r[-1]:
        r.append(A[i])
    else:
        idx = bisect_left(r, A[i])
        r[idx] = A[i]
        
    dpr[i] = len(r)
    
A = A[::-1]
l = [A[0]]
for i in range(1, N):
    if  A[i] > l[-1]:
        l.append(A[i])
    else:
        idx = bisect_left(l, A[i])
        l[idx] = A[i]

    dpl[i] = len(l)
    
ans = 1
for i in range(N):
    ans = max(ans, dpr[i] + dpl[N-1-i] - 1)
    
print(ans)
