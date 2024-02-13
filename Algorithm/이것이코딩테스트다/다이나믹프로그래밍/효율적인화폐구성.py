N, M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))
    
arr.sort(reverse=True) # 큰값을 기준으로 정렬한다. 불가능 할때는 -1 Return 해야함.
count = 0

dp = [0] * M

for money in arr:
    if(M > money):
        dp[money] = 1

idx = min(M+1, max(arr)+1)
while(idx > M):
    min = 0
    for money in arr:
        if(min > dp[idx-money]):
            min = dp[idx-money]
    
    dp[idx] = min + 1
    idx +=1
    
print(count, M)

dy = [10001] * (M+1)
dy[0] = 0

for i in range(N) :
    for j in range(arr[i], M+1):
        if(arr[j-arr[i]] != 10001) :
            arr[j] = min(arr[j, arr[j-arr[i]] + 1])