import sys
from pprint import pprint
input = sys.stdin.readline

HOR = 0 # 가로
VER = 1 # 세로
CROSS = 2 # 대각선

N = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)+1):
        graph[i][j] = temp[j-1]



dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(3)]
movetype = (((0, -1, HOR), (-1, -1, CROSS)), ((-1, 0, VER), (-1, -1, CROSS)), ((-1, 0, HOR), (0, -1, VER), (-1, -1, CROSS)))

dp[HOR][1][2] = 1 # 출발값

for i in range(1, N+1):
    for j in range(3, N+1):
        for t in range(3):
            for dy, dx, mt in movetype[t]:
                ny, nx = i + dy, j + dx
                if N >= ny > 0 and N >= nx > 0:
                    if (mt == CROSS and t == CROSS) and graph[i][j] == 0 and graph[i-1][j] == 0 and graph[i][j-1] == 0: # 대각선에서 왔다면
                        dp[t][i][j] += dp[mt][ny][nx]
                    elif (t == HOR or t == VER) and graph[i][j] == 0: # 가로, 혹은 세로에서 왔다면
                        dp[t][i][j] += dp[mt][ny][nx]

for d in dp:
    pprint(d)
    print(d[N][N])

