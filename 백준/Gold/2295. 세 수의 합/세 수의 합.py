import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

arr_sum = []
arr_sub = []
for a in arr:
    for b in arr:
        arr_sum.append(a+b)
        if a >= b:
            arr_sub.append([a-b, a])
            
def find(arr, v):
    start, end = 0, len(arr)-1
    idx = -1
    while end >= start:
        mid = (start + end) // 2
        if arr[mid][0] >= v:
            idx = mid
            end = mid - 1
        else:
            start = mid + 1
    return idx

arr_sum.sort(reverse=True)
arr_sub.sort()

ans = []
for v in arr_sum:
    idx = find(arr_sub, v)
    if idx != -1 and idx != len(arr_sub):
        if v == arr_sub[idx][0]:
            ans.append(arr_sub[idx][1])
            
ans.sort()
print(ans[-1])
