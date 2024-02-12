# https://www.acmicpc.net/problem/2470
import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()

pleft = 0
pright = N-1

ans = [data[pleft], data[pright]]
min_cost = abs(data[pleft] + data[pright])

while pleft < pright:
    cost = data[pleft] + data[pright]

    if min_cost > abs(cost):
        min_cost = abs(cost)
        ans = [data[pleft], data[pright]]
        if cost == 0:
            break
        
    if cost > 0:
        pright -= 1
    else:
        pleft += 1
    
print(ans[0], ans[1])