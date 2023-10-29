# https://www.acmicpc.net/problem/2447
import sys
input = sys.stdin.readline

k = int(input())

def dfs(n):
    if n == 1:
        return ['*']
    
    star = dfs(n//3)
    result = []
    for s in star:
        result.append(s*3)
    
    for s in star:
        result.append(s + ' '*(n//3) + s)
        
    for s in star:
        result.append(s*3)
        
    return result

print('\n'.join(dfs(k)))