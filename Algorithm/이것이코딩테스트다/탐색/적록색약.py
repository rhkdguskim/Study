# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다.
# 크기가 NxN인 그리드의 각 칸에 r,g,b 중 하나를 색칠한 그림이 있다. 구역은 같은 색으로 이루어져있고
# 같은 색상이 상하좌우로 인접해 있는경우에 두 글자는 같은 구역에 속한다.
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(str, input())))

visited = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]

def dfs(i, j, str):
    if (N > i >= 0 and N > j >= 0 ):  # 유효성 검사
        if (visited[i][j] == False) and (arr[i][j] == str):
            visited[i][j] = True
            dfs(i+1,j, str)
            dfs(i-1,j, str)
            dfs(i,j+1, str)
            dfs(i,j-1, str)
            return True
        else :
            return False
    else :
        return False

def dfs2(i, j, str):
    if not (N > i >= 0 and N > j >= 0 ):  # 유효성 검사
        return False
    
    if(arr[i][j] == 'G'):
        arr[i][j] = 'R'
        str='R'
    if (visited2[i][j] == False) and (arr[i][j] == str):
        visited2[i][j] = True
        dfs2(i+1,j, str)
        dfs2(i-1,j, str)
        dfs2(i,j+1, str)
        dfs2(i,j-1, str)
    else :
        return False
    
    return True


count = 0
count2 = 0
for i in range(N):
    for j in range(N):
        if(dfs(i,j,'R') == True): 
            count+= 1
        elif(dfs(i,j,'G') == True):
            count+= 1
        elif(dfs(i,j,'B') == True):
            count+= 1
            
for i in range(N):
    for j in range(N):           
        if(dfs2(i,j,'R') == True): 
            count2+= 1
        elif(dfs2(i,j,'G') == True):
            count2+= 1
        elif(dfs2(i,j,'B') == True):
            count2+= 1

print(count, count2)