# https://www.acmicpc.net/problem/1275
import sys
input = sys.stdin.readline

def update(node, value, fwt):
    while node < N+1:
        fwt[node] += value
        node += node & (-node)
        
def query(node, fwt):
    ans = 0
    while node >= 1:
        ans += fwt[node]
        node -= node & (-node)
    
    return ans

def prefix_sum(start, end, fwt):
    return query(end, fwt) - query(start-1, fwt)


N, Q = map(int, input().split())

data = list(map(int, input().split()))

fwt = [0 for _ in range(N+1)]

for i in range(1, N+1):
    update(i, data[i-1], fwt)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x >= y:
        print(prefix_sum(y, x, fwt))
    else:
        print(prefix_sum(x, y, fwt))
        
    diff = b - data[a-1]
    data[a-1] = b
    update(a, diff, fwt)
    