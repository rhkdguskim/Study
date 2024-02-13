# https://www.acmicpc.net/problem/1275
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

data = list(map(int, input().split()))

tree = [0 for _ in range(4*N)]

def init(start, end, node):
    if start == end:
        tree[node] += data[start]
        return tree[node]
    else:
        mid = ( start + end ) // 2
        tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
        return tree[node]
        
def update(start, end, node, idx, diff):
    if idx < start or idx > end:
        return
    
    tree[node] += diff
    
    if start == end:
        return
    
    mid = ( start + end ) // 2
    update(start, mid, node * 2, idx, diff)
    update(mid + 1, end, node * 2 + 1, idx, diff)

def query(start, end, node, left, right):
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = ( start + end ) // 2
    lsum = query(start, mid, node * 2, left, right)
    rsum = query(mid + 1, end, node * 2 + 1, left, right)
    return lsum + rsum
        
init(0, N-1, 1)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x >= y:
        x, y = y, x
        
    print(query(0, N-1, 1, x-1, y-1))
    diff = b - data[a-1]
    update(0, N-1, 1, a-1, diff)
    data[a-1] = b