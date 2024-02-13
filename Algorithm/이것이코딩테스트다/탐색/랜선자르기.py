#https://www.acmicpc.net/problem/1654
K, N = map(int, input().split()) # 오영식이 가지고 있는 랜선의 개수, 필요한 랜선의 개수 N
lancable = []

for _ in range(K):
    lancable.append(int(input()))
    
lancable.sort()

start = 1
end = lancable[-1]

result = 0
if K == 1:
    print(lancable[0]//N)
else:
    while start < end:
        mid = (start + end) // 2 # LAN케이블을 자르는 길이
        sum = 0
        for i in range(K):
            sum += (lancable[i] // mid)
            

        if sum >= N: # 개수가 더 많을경우 범위를 좁혀 탐색한다.
            result = max(result, mid)
            start = mid+1
        else: # 개수가 더 적을경우 범위를 넓혀 탐색한다.
            end = mid
            
    print(result)