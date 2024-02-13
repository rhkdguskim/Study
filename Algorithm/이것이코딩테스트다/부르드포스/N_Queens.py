#https://www.acmicpc.net/problem/9663
N = int(input())
count = 0

def isvalied(queens,i,j):
    if N > i >=0 and N > j >= 0:
        for queen in queens:
            k, n = queen
            if i == k or j == n or abs(i-k) == abs(n-j):
                return False
        
        return True 
    else:
        return False
    

def dfs(i,j):
    global count
    global queens
    if len(queens) == N:
        count += 1
        return
        
    for k in range(N):
        if isvalied(queens, i+1, k):
            queens.append([i+1,k])
            dfs(i+1, k)
            queens.pop()
  
queens = []
for i in range(N):
    queens.append([0,i])
    dfs(0,i)
    queens.pop()
    
print(count)