# https://www.acmicpc.net/problem/2473
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()

min_value = sys.maxsize
ans = [-1, -1, -1]
for cur in range(N-2):
    left = cur+1
    right = N-1
    while left < right:
        cost = data[cur] + data[left] + data[right]
        
        if min_value > abs(cost):
            min_value = abs(cost)
            ans = [data[cur], data[left], data[right]]
        
        if cost == 0:
            break
        
        if cost > 0:
            right -= 1
        else:
            left += 1
            
print(ans[0], ans[1], ans[2])
            
        
            
        