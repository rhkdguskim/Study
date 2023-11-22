# https://www.acmicpc.net/problem/14502
# 완전탐색(브루트포스) 방식으로 문제를 해결한다.
import copy
N, M = map(int, input().split()) # N은 행, M은 열

rdtable = []
virus = []
 
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        if arr[j] == 2:
            virus.append([i,j])
    rdtable.append(arr)
    

def checkSaveArea(rdtable):
    count = 0
    for i in range(N):
        for j in range(M):
            if rdtable[i][j] == 0:
                count += 1
                
    return count

def dfs(i,j, table): # dfs로 바이러스를 감염시킨다
    if N > i >=0 and M > j >= 0 and table[i][j] == 0:
        table[i][j] = 2
        
        dfs(i+1,j, table)
        dfs(i-1,j, table)
        dfs(i,j+1, table)
        dfs(i,j-1, table)
    

def solve(rdtable, num):
    table = copy.deepcopy(rdtable)
    result = 0
    if num == 3:
        for i,j in virus:
            dfs(i+1,j,table)
            dfs(i-1,j,table)
            dfs(i,j+1,table)
            dfs(i,j-1,table)
        
        return checkSaveArea(table)
        
    
    for i in range(N):
        for j in range(M):
            if table[i][j] == 0:
                table[i][j] = 1
                result = max(result, solve(table, num+1))
                table[i][j] = 0
    return result

print(solve(rdtable, 0))
        
    
