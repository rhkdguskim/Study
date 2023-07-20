# https://www.acmicpc.net/problem/12100
# 1. 구현문제와, 백트래킹 문제
# 2. 상,하,좌,우 모든 가능한 곳을 가본다.
import copy
N = int(input())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))



def up(table, visited):
    for i in range(N):
        start = N-1
        while start > 0:
            #print(start)
            if table[start][i] == 0: # 자기자신이 0인경우 다음탐색
                start -= 1
                continue
            
            if table[start-1][i] == 0: # 자기자신위에가 0인경우 자기자신을 0으로 옮긴다.
                table[start-1][i] = table[start][i]
                table[start][i] = 0
                start -= 1
            else:
                if (table[start-1][i] == table[start][i]) and not (visited[start-1][i] and visited[start][i]):# 숫자가 같고 둘다 합쳐진게 아니라면
                    table[start-1][i] = table[start-1][i] + table[start][i] # 값을 합친다.
                    visited[start-1][i] = True # 합쳐진거 표시해준다.
                    table[start][i] = 0 # 자기자신은 0으로 리셋해준다.
                    
                start -= 1
                    
def down(table, visited):
    for i in range(N):
        start = 0
        while N-1 > start:
            if table[start][i] == 0: # 자기자신이 0인경우 다음탐색
                start += 1
                continue
            
            if table[start+1][i] == 0: # 자기자신위에가 0인경우 자기자신을 0으로 옮긴다.
                table[start+1][i] = table[start][i]
                table[start][i] = 0
                start += 1
            else:
                if (table[start+1][i] == table[start][i]) and not (visited[start+1][i] and visited[start][i]):# 숫자가 같고 둘다 합쳐진게 아니라면
                    table[start+1][i] = table[start+1][i] + table[start][i] # 값을 합친다.
                    visited[start+1][i] = True # 합쳐진거 표시해준다.
                    table[start][i] = 0 # 자기자신은 0으로 리셋해준다.
                    
                start += 1
                    
def left(table, visited):
    for i in range(N):
        start = N-1
        while start > 0:
            if table[i][start] == 0: # 자기자신이 0인경우 다음탐색
                start -= 1
                continue
            
            if table[i][start-1] == 0: # 자기자신위에가 0인경우 자기자신을 0으로 옮긴다.
                table[i][start-1] = table[i][start]
                table[i][start] = 0
                start -= 1
            else:
                if (table[i][start-1] == table[i][start]) and not (visited[i][start-1] and visited[i][start]):# 숫자가 같고 둘다 합쳐진게 아니라면
                    table[i][start-1] = table[i][start-1] + table[i][start] # 값을 합친다.
                    visited[i][start-1] = True # 합쳐진거 표시해준다.
                    table[i][start] = 0 # 자기자신은 0으로 리셋해준다.
                    
                start -= 1
                
def right(table, visited):
    #print(table, "before right")
    for i in range(N):
        start = 0
        while N-1 > start:
            if table[i][start] == 0: # 자기자신이 0인경우 다음탐색
                start += 1
                continue
            
            if table[i][start+1] == 0: # 자기자신위에가 0인경우 자기자신을 0으로 옮긴다.
                table[i][start+1] = table[i][start]
                table[i][start] = 0
                start += 1
            else:
                if (table[i][start+1] == table[i][start]) and not (visited[i][start+1] and visited[i][start]):# 숫자가 같고 둘다 합쳐진게 아니라면
                    table[i][start+1] = table[i][start+1] + table[i][start] # 값을 합친다.
                    visited[i][start+1] = True # 합쳐진거 표시해준다.
                    table[i][start] = 0 # 자기자신은 0으로 리셋해준다.
                    
                start += 1
            
    #print(table, "after right")

maxvalue = 0
count = 0
def dfs(table, visited, pos, depth):
    global maxvalue
    global count
    
    newtable = copy.deepcopy(table)
    newvisited = copy.deepcopy(visited)
    
    count += 1
    if depth == 5:
        #print(newtable)
        for i in range(N):
            maxvalue = max(maxvalue, max(newtable[i]))
        return
    
    if pos == 0:
        up(newtable, newvisited)
    elif pos == 1:
        down(newtable, newvisited)
    elif pos == 2:
        left(newtable, newvisited)
    else :
        right(newtable, newvisited)
        
    for i in range(4):
        dfs(newtable, newvisited, i, depth+1)


visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(4):
    dfs(table, visited, i, 0)
    

print(maxvalue)
#print(count)