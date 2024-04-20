# https://www.acmicpc.net/problem/8980
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
M = int(input())

delivery = []
house = [C for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    delivery.append((start, end, cost))
    
delivery.sort(key=lambda x:x[1])

ans = 0
for start, end, cost in delivery:
    temp = C
    for i in range(start, end):
        temp = min(temp, house[i])
    temp = min(temp, cost)
    for i in range(start, end):
        house[i] -= temp
    ans += temp
    
print(ans)