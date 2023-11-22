# https://www.acmicpc.net/problem/12100
# 1. 구현문제와, 백트래킹 문제
# 2. 상,하,좌,우 모든 가능한 곳을 가본다.
import copy
N = int(input())
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))


def up(table):
    for j in range(N):
        pointer = 0
        for i in range(1, N):
            if table[i][j]:
                temp = table[i][j]
                table[i][j] = 0
                
                if table[pointer][j]:
                    if table[pointer][j] == temp: # 포인터와 같다면
                        table[pointer][j] = temp*2
                        pointer += 1
                    else:
                        pointer += 1
                        table[pointer][j] = temp
                        
                else:
                    table[pointer][j] = temp
                
    return table
                    
def down(table):
    for j in range(N):
        pointer = N-1
        for i in range(N-2, -1, -1):
            if table[i][j]:
                temp = table[i][j]
                table[i][j] = 0
                if table[pointer][j]:
                    if table[pointer][j] == temp: # 포인터와 같다면
                        table[pointer][j] = temp*2
                        pointer -= 1
                    else:
                        pointer -= 1
                        table[pointer][j] = temp
                        
                else:
                    table[pointer][j] = temp
                
    return table
                    
def left(table):
    for i in range(N):
        pointer = 0
        for j in range(1, N):
            if table[i][j]:
                temp = table[i][j]
                table[i][j] = 0
                if table[i][pointer]:
                    if table[i][pointer] == temp: # 포인터와 같다면
                        table[i][pointer] = temp*2
                        pointer += 1
                    else:
                        pointer += 1
                        table[i][pointer] = temp
                        
                else:
                    table[i][pointer] = temp
                
    return table
                
def right(table):
    for i in range(N):
        pointer = N-1
        for j in range(N-2, -1, -1):
            if table[i][j]:
                temp = table[i][j]
                table[i][j] = 0
                if table[i][pointer]:
                    if table[i][pointer] == temp: # 포인터와 같다면
                        table[i][pointer] = temp*2
                        pointer -= 1
                    else:
                        pointer -= 1
                        table[i][pointer] = temp
                        
                else:
                    table[i][pointer] = temp
                
    return table
                
def move(pos, table):
    if pos == 0:
        return up(table)
    elif pos == 1:
        return down(table)
    elif pos == 2:
        return left(table)
    else :
        return right(table)

def dfs(table, depth):
    if depth == 5:
        return max(map(max, table))
    
    maxvalue = 0
    for i in range(4):
        maxvalue = max(maxvalue, dfs(move(i, copy.deepcopy(table)), depth+1))
    
    return maxvalue

print(dfs(table, 0))