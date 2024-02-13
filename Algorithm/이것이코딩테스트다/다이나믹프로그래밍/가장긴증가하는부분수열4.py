# https://www.acmicpc.net/problem/14002
N = int(input())
arr = list(map(int,input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

maxdp = max(dp)
print(maxdp)

maxidx = dp.index(max(dp))

newlist = []
while maxidx >= 0:
    if dp[maxidx] == maxdp:
        newlist.append(arr[maxidx])
        maxdp-=1
        
    maxidx-=1

newlist.reverse()
print(*newlist)