# https://www.acmicpc.net/problem/5904

def dfs(N, cur, depth):
    if 3 >= N:
        print(N)
        if N == 1:
            print("m")
        else:
            print("o")
        return
    cost = cur*3 + 3 + depth
    N -= cost   
    dfs(N, cost, depth+1) 
    
dfs(11, 0, 0)
    