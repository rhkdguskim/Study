# https://www.acmicpc.net/problem/11054
from bisect import bisect_left
N = int(input())
arr = list(map(int, input().split()))

leftdp = [1 for _ in range(N+1)]
rightdp = [1 for _ in range(N+1)]
temp = [arr[0]]

for i in range(N):
    if arr[i] > temp[-1]:
        temp.append(arr[i])
        leftdp[i] = len(temp)
    else :
        idx = bisect_left(temp, arr[i])
        temp[idx] = arr[i]
        leftdp[i] = idx + 1

arr.reverse()
temp = [arr[0]]
for i in range(N):
    if arr[i] > temp[-1]:
        temp.append(arr[i])
        rightdp[i] = len(temp)
    else :
        idx = bisect_left(temp, arr[i])
        temp[idx] = arr[i]
        rightdp[i] = idx + 1

for i in range(len(leftdp)):
    print(leftdp[i]+rightdp[i])