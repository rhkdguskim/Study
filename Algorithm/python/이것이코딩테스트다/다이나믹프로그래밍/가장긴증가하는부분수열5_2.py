# https://www.acmicpc.net/problem/14003
import sys

input = sys.stdin.readline

import bisect
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

ans=[0]*n
lis = [-1000000001]
for i in range(n):
    if arr[i]> lis[-1]:
        lis.append(arr[i])
        ans[i]=len(lis) # 추적하기 위한 값 업데이트
    else:
        temp = bisect.bisect_left(lis, arr[i])
        lis[temp] = arr[i]
        ans[i] = temp + 1 # 추적하기위한 값 업데이트

temp = [0] * len(lis)
cnt = len(lis)
for i in range(len(arr) - 1, -1, -1):
    if ans[i] == cnt:
        cnt-=1
        temp[cnt] = arr[i]

print(ans)
l = len(lis)
print(l-1)
print(*temp[1:])