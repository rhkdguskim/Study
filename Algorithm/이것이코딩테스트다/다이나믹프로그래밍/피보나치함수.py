N = int(input())

def fibo(n, dp):
    if len(dp[n]) > 0:
        return dp[n]
    
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        dp[n] = [0, 0]
        fibo_n_1 = fibo(n-1, dp)
        fibo_n_2 = fibo(n-2, dp)
        dp[n][0] = fibo_n_1[0] + fibo_n_2[0] # 0번째 노드에는 0의 개수가 누적
        dp[n][1] = fibo_n_1[1] + fibo_n_2[1] # 1번째 노드에는 1의 개수가 누적
        return dp[n]

dp = [[] for _ in range(41)]

for _ in range(N):
    data = int(input())
    result = fibo(data, dp)
    print(result[0], result[1])