#https://www.acmicpc.net/problem/14500

# ㅗ 모양
shape = [[[0,0], [-1,0], [-1,1], [-2,0]], [[0,0], [-1,0], [-1,-1], [-2,0]],
       [[0,0], [-1,0], [-1,-1], [-1,1]], [[0,0], [0,1], [0,2], [-1,1]]]

table = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
for _ in range(N):
    table.append(list(map(int, input().split())))

visited = [[False for _ in range(M)] for _ in range(N)]

result = 0

def SpiecalShape(i,j):
    global result
    for n in range(len(shape)):
        sum = 0
        for m in range(len(shape[n])):
            x, y = shape[n][m][0]+i, shape[n][m][1]+j
            if N > x >= 0 and M > y >= 0:
                sum += table[x][y]
                
        result = max(sum,result)
        
    
    
def dfs(i,j,sum,depth):
    global result
    if N > i >=0 and M > j >= 0:
        sum += table[i][j]
        if depth == 3:
            result = max(result, sum)
            return
        
        for k in range(4):
            x, y = dx[k]+i, dy[k]+j
            if N > x >=0 and M > y >= 0 and not visited[x][y]:
                visited[x][y] = True
                dfs(x,y, sum, depth+1)
                visited[x][y] = False
    

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j,0,0)
        visited[i][j] = False
        SpiecalShape(i,j)
        
        
print(result)