# https://www.acmicpc.net/problem/11726
n = int(input())

dp = [0] * (1000+1)
dp[1] = 1
dp[2] = 2
def f(n):
    if(dp[n] != 0):
        return dp[n] 
    else:
        dp[n] = f(n-1) + f(n-2)
        return dp[n]
        
print(f(n)%10007)