# https://www.acmicpc.net/problem/15649
N , M = map(int, input().split())

def dfs(i, char):
    char += str(i)
    if len(char) == M:
        for i in range(len(char)):
            if i == len(char) -1:
                print(char[i])
            else:
                print(char[i], end=' ')
    
    for k in range(1, N+1):
        if not str(k) in char:
            dfs(k, char)
            
for i in range(1, N+1):
    char = ''
    dfs(i, char)