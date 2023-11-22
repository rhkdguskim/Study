import sys
sys.setrecursionlimit(10**6)
X = int(input())
INF = int(10e9)
dp = [INF for _ in range(X+1)] # X+1 크기만큼의 배열을 생성


def makeNumber1(number):
    if number >= X:
        return 0

    if X >= number * 3:
        dp[number*3] = makeNumber1(number*3)
        dp[number] = min(dp[number*3]+1, dp[number])
    if X >= number * 2:
        dp[number*2] = makeNumber1(number*2)
        dp[number] = min(dp[number*2]+1, dp[number])
    if X >= number + 1:
        dp[number+1] = makeNumber1(number+1)
        dp[number] = min(dp[number+1]+1, dp[number])
    
    return dp[number]
    
result = makeNumber1(1)
if result == INF:
    print(0)
else:
    print(result)