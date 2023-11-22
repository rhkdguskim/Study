
N = int(input())
dp = [[0 for _ in range(1 << 10)] for _ in range(10)]

for i in range(1, 10):
    dp[i][1<<i] = 1
    
mod = 1000000000

for _ in range(1, N):
    newdp = [[0 for _ in range(1 << 10)] for _ in range(10)]
    for i in range(10):
        for k in range(1024):
            if i > 0:
                newdp[i][k | (1<<i)] += (dp[i-1][k] % mod)
            if i < 9:
                newdp[i][k | (1<<i)] += (dp[i+1][k] % mod)
    
    dp = newdp
    

print(sum(dp[i][1023] for i in range(len(dp))) % mod)