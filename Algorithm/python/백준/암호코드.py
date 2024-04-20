# https://www.acmicpc.net/problem/2011
import sys
input = sys.stdin.readline

password = ['0'] + list(str(input().strip()))
dp = [0] * len(password)
dp[0], dp[1] = 1, 1

if password[1] == '0':
    print(0)
    exit()

for i in range(2, len(dp)):
    first = int(password[i])
    second = int(password[i]) + int(password[i-1]) * 10
    
    if first > 0:
        dp[i] += dp[i-1]
    
    if  10 <= second <= 26:
        dp[i] += dp[i-2]

print(dp[-1]%1000000)