#https://www.acmicpc.net/problem/11066
def filesum(arr, dp, depth):
    newarr = arr[:]
    if 2 >= len(newarr):
        dp[depth] = sum(newarr)
        return dp[depth]
    
    dp[depth] = min(filesum(newarr[1:], dp,depth+1) + newarr[0], filesum(newarr[:len(newarr)-1], dp,depth+1)+ newarr[-1])
    return dp[depth]

T = int(input())

for _ in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    dp = [0 for _ in range(K)]
    print(dp)
    filesum(arr, dp, 0)
    print(dp)

