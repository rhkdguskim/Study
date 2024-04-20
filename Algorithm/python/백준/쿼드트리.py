# https://www.acmicpc.net/problem/1992
import sys
input = sys.stdin.readline

N = int(input())
type = [(0,0), (0,1), (1,0), (1,1)]
data = []

for _ in range(N):
    data.append(list(input().strip()))

def quard_tree(i, j, size):
    if size == 1:
        return data[i][j]
    
    result = []
    cost = size//2
    for dy, dx in type:
        result.append(quard_tree((i + dy*cost),(j + dx*cost), (cost)))
    
    temp = result[0]
    if len(temp) == 1:
        for i in range(1, 4):
            if temp != result[i]:
                return '(' + ''.join(result) + ')'
        
        return result[0]
    else:
        return '(' + ''.join(result)+ ')'
    
print(quard_tree(0,0,N))

        
    