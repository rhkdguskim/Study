from collections import defaultdict
import sys
input = sys.stdin.readline

ab_sum = defaultdict(int)

N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
    
for a in A:
    for b in B:
        ab_sum[a+b] += 1

ans = 0
for c in C:
    for d in D:
        ans += ab_sum[-(c+d)]
        
print(ans)