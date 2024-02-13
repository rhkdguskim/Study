# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어있다. 이때, 수열 x가 등정하는 횟수를 계산하여라
import sys
input = sys.stdin.readline

N, x = map(int, input().split())
arr = list(map(int, input().split()))

# 가장 오른쪽 끝에 있는 idx 찾기
def right_idx():
    start = 0
    end = len(arr) - 1
    idx = None
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] <= x:
            idx = mid
            start = mid + 1
        else:
            end = mid - 1
    return idx
        

# 가장 왼쪽 끝에있는 idx 찾기
def left_idx():
    start = 0
    end = len(arr) - 1
    idx = None
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] >= x:
            idx = mid
            end = mid - 1
        else:
            start = mid + 1
    return idx

left = left_idx()
right = right_idx()

if left == None:
    print(-1)
else:
    print(right - left + 1)