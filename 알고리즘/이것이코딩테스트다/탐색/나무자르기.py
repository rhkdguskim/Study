#https://www.acmicpc.net/problem/2805
N, M = map(int, input().split()) # 나무의 개수, M미터의 나무를 가져가야함.

tree = list(map(int ,input().split()))
    
tree.sort() # 이분 탐색을 위해 정렬한다.

start = 1
end = tree[-1]

result = int(10e9)
ans = 0
if N == 1:
    print(tree[0] - M)
else:
    while start < end:
        mid = ( start + end ) // 2 # H값을 선정
        sum = 0
        for i in range(N):
            cost = tree[i] - mid
            if cost > 0:
                sum += cost
            
        if sum >= M: # 값이 큰경우 작은 범위로 탐색하게 한다. 높이를 늘린다.
            if result > sum:
                result = sum
                ans = mid
            start = mid+1
        else: # 값이 작은경우 큰 범위로 탐색하게 한다. 높이를 낮춘다.
            end = mid
              
    print(ans)
        
