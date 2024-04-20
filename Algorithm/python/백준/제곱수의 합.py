# https://www.acmicpc.net/problem/1699
import sys
import math
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]

i = 1
cnt = 1
while N >= i:
    dp[i] = 1
    cnt += 1
    i = cnt**2
    
def find(num):
    return int(math.sqrt(num)) ** 2
    
for i in range(2, N+1):
    start = i
    while start >= 1:
        num = find(start)
        if num == i:
            break
        
        dp[i] += dp[num]
        start -= num
        
print(dp[N])