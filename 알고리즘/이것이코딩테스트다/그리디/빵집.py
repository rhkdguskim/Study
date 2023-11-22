# https://www.acmicpc.net/problem/3109
R, C = map(int, input().split()) # R은 행 C는 열
arr = []
visited = [[False for _ in range(C)] for _ in range(R)]

for i in range(R):
    char = str(input())
    arr.append(char)
    for j in range(len(char)):
        if char[j] == 'x':
            visited[i][j] = True
            
counter = 0

def dfs(i,j):
    global counter
    if R > i >=0 and C > j >=0 and not visited[i][j]:
        if j == C-1:
            counter +=1
            return True
        
        visited[i][j] = True
        if dfs(i-1,j+1): # 오른쪽 대각선 위
            return True
        if dfs(i,j+1): # 오른쪽
            return True
        if dfs(i+1,j+1): # 오른쪽 대각선 아래
            return True
    else:
        return False
    
for i in range(R):
    dfs(i,0)
     
print(counter)