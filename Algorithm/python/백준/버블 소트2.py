#https://www.acmicpc.net/problem/1377
# 10 1 5 2 3 1
# 1 5 2 3 10 2
# 1 2 3 5 10 3
# --> 3

# 1 3 5 7 9 1
# --> 1
import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append((int(input()), i))

new_arr = deepcopy(arr)
new_arr.sort()

ans = 0
for i in range(N):
    ans = max(ans, new_arr[i][1] - arr[i][1])
    
print(ans+1)