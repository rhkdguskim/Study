# https://www.acmicpc.net/problem/1285
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(input().strip()) for _ in range(N)]

# 동전을 뒤집을 수 있는경우의수는 행의 기준으로 2^n 이다.
# 해당행을 뒤집은경우, 뒤집지 않은경우가 2가지이고, 행의 개수가 n개 이니까 2^n이다.
rev_graph = [ graph[i][:] for i in range(N)]


for i in range(N):
    for j in range(N):
        if rev_graph[i][j] == 'T':
            rev_graph[i][j] = 'H'
        else:
            rev_graph[i][j] = 'T'
            
ans = N**2 + 1
for b in range(1 << N): # 비트마스킹
    temp = []
    for i in range(N):
        if b & (1 << i): # 뒤집은경우
            temp.append(rev_graph[i][:])
        else:
            temp.append(graph[i][:])
    
    t_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if temp[j][i] == 'T':
                cnt += 1
                
        t_cnt += min(cnt, N-cnt)
        
    ans = min(t_cnt, ans)
    
print(ans)