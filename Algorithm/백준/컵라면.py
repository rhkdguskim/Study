# https://www.acmicpc.net/problem/1781
import sys
input = sys.stdin.readline

N = int(input())

parent = [i for i in range(N+1)]

def union(v1, v2):
    p1 = parent[v1]
    p2 = parent[v2]
    if p1 > p2:
        parent[p1] = p2
    else:
        parent[p2] = p1
        
def find(v1):
    if parent[v1] != v1:
        parent[v1] = find(parent[v1])
        return parent[v1]
    else:
        return parent[v1]

problem = []
for _ in range(N):
     a, b = map(int, input().split())
     problem.append((a, b)) # 데드라인, 컵라면수

problem.sort(key=lambda x:-x[1])

ans = 0
for deadline, score in problem:
    day = find(deadline)
    if day > 0:
        union(day, day-1)
        ans += score
        
print(ans)
        
    