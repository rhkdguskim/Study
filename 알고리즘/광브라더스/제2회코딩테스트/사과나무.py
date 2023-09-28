# table[a][b][N] = table[a][b+1][N-1] + table[a+1][b][N-1] + table[a][b][1] + table[a+N-1][b+N-1][1] - table[a+1][b+1][N-2]
import pprint
N = int(input())

table = [[[-300001 for _ in range(N)] for _ in range(N)] for _ in range(N+1)]

apple = []
for _ in range(N):
    apple.append(list(map(int, input().split())))
    
for i in range(N):
    for j in range(N):
        table[1][i][j] = apple[i][j]
        table[0][i][j] = 0
            
for n in range(2, N+1):
    for i in range(N):
        for j in range(N):
            if N > i+1 >= 0 and N > j+1 >= 0:
                table[n][i][j] = table[n-1][i][j+1] + table[n-1][i+1][j] - table[n-2][i+1][j+1] + table[1][i][j] + table[1][n-1][n-1]
            
maxvalue = -300001
for n in range(1, N+1):
    for i in range(N):
        for j in range(N):
            if N > i+1 >= 0 and N > j+1 >= 0:
                maxvalue = max(table[n][i][j],maxvalue)

pprint.pprint(table)
print(maxvalue)