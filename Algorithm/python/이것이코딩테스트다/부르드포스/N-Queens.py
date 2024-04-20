N = int(input())

count = 0
def dfs(i,j, table):
    global count
    queentable = table[:]
    if N > i >=0 and N > j >=0 and not queentable[i][j]:
        
        if i == N-1:
            count += 1
        
        for k in range(N): # 세로
            queentable[i][k] = 1
            
        for k in range(N): # 가로
            queentable[k][j] = 1
            
        for k in range(N): # 대각선
            for n in range(N):
                if k-i == n-j:
                    queentable[k][n] = 1
        
        print(i,j)
        print(queentable)
        for k in range(N):        
            dfs(i+1, k, queentable)
    

for i in range(N):
    table = [[0 for _ in range(N)] for _ in range(N)] # NxN 테이블 생성
    dfs(0,i, table)
    
print(count)