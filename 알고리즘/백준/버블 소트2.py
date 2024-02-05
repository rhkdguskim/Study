#https://www.acmicpc.net/problem/1377
# 10 1 5 2 3 1
# 1 5 2 3 10 2
# 1 2 3 5 10 3
# --> 3

# 1 3 5 7 9 1
# --> 1
import sys
from copy import deepcopy
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

new_arr = deepcopy(arr)
new_arr.sort()

cursor = 0
cnt = 1
for num in arr:
    idx = bisect_left(new_arr, num)
    if cursor != idx and new_arr[cursor] != num:
        cnt += 1
    else:
        cursor += 1
        
print(cnt)