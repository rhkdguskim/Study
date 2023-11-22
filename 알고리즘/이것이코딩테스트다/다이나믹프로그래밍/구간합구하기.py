# https://www.acmicpc.net/problem/11660
N , M = map(int, input().split()) #표의 크기 N, 횟수 M

table = []
for _ in range(N): # 테이블 생성
    table.append(list(map(int, input().split())))
    
answer = []
for _ in range(M): # x,y 좌표
    x1, y1, x2, y2 = map(int, input().split())
    answer.append([x1, y1, x2, y2])
    
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]


for i in range(1,N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + table[i-1][j-1]

def rangeSum(x1, y1, x2, y2):
    return dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]

for x1,y1,x2,y2 in answer:
    print(rangeSum(x1,y1,x2,y2))
    