# https://www.acmicpc.net/problem/11053
N = int(input())
li = list(map(int,input().split()))
dp = [li[0]]

for i in range(1,N):
    if li[i] > dp[-1]:
        dp.append(li[i])
    else:
        j = len(dp)-1
        while j > 0:
            if dp[j-1] < li[i]:
                break
            j -= 1
        dp[j] = li[i]
print(len(dp))