import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

start = 0
end = len(arr) - 1
ans = -1
while start <= end:
    mid = (start + end ) // 2
    
    if arr[mid] == mid:
        ans = mid
        break
    elif arr[mid] > mid: # 배열이 더 크다면 오른쪽에 있는 값들은 볼 필요 없다.
        end = mid - 1
    else: # 배열이 더 작다면 왼쪽에 있는값들은 볼 필요 없다.
        start = mid + 1
        
print(ans)