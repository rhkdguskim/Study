# https://www.acmicpc.net/problem/2775
testnum = int(input())
stare = []
addr = []
for _ in range(testnum):
    stare.append(int(input()))
    addr.append(int(input()))
    
dp = [[0 for _ in range(max(addr)+1)] for _ in range(max(stare)+1)]

for i in range(0, len(dp[0])):
    dp[0][i] = i

for j in range(0, len(dp)):
    dp[j][0] = 0

for i in range(1, len(dp)):
    for j in range(1, len(dp[i])):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]


for i in range(testnum):
    print(dp[stare[i]][addr[i]])