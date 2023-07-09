# https://www.acmicpc.net/problem/2156
import sys 
sys.setrecursionlimit(10**6)
n = int(input())
item = []
for _ in range(n):
    item.append(int(input()))

dptable = [0 for _ in range(sum(item)+1)]
def dp(n, depth):
    if depth == 3:
        return item[n]
    
    if n == 0:
        return 0
    
    if depth == 2:
        dptable[n-1] = dp(n-1, 0)
        result = dptable[n-1]
    else:
        dptable[n-1] = max(dp(n-1, depth+1) + item[n-1], dp(n-1, 0))
        result = dptable[n-1]
    
    return result

print(dp(n,0))