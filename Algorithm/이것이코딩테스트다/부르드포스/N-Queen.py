# https://www.acmicpc.net/problem/9663
# 퀸은 가로, 세로, 대각선 만 공격가능하다.
N = int(input())
newarr = []
def dfs(i,j, queens):
    if not (N > i >=0 and N > j >= 0):
        return
    
    queens.append([i,j])
    
    for idx in range(len(queens) - 1):
        if queens[idx][0] == i: #세로 방문 불가
            return
        if queens[idx][1] == j: #가로 방문 불가
            return
        if abs(queens[idx][0] - i) == abs(queens[idx][1] - j): #대각선인경우 방문불가
            return
    
    if(len(queens) == N): # 퀸이 모두 세워진경우
        newarr.append(queens)
        return
    
    for k in range(N):
        dfs(i+1,k, queens)
        queens.pop()

        
for x in range(N):
    queens = []
    dfs(0,x, queens)
    
print(len(newarr))