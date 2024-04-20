# https://www.acmicpc.net/problem/7578
import sys

input = sys.stdin.readline
N = int(input())

temp_A = list(map(int, input().split()))
temp_B = list(map(int, input().split()))
tree = [0 for _ in range(4*N)]

B = {}

for i in range(N):
    B[temp_B[i]] = i

def update(start, end, node, idx):
    if idx < start or idx > end:
        return
    
    tree[node] += 1
    
    if start == end:
        return
    
    mid = ( start + end ) // 2
    update(start, mid, node * 2, idx)
    update(mid + 1, end, node * 2 + 1, idx)

def query(start, end, node, left, right):
    if left > end or right < start:
        return 0
    
    if start >= left and end <= right:
        return tree[node]
    
    mid = ( start + end ) // 2
    lsum = query(start, mid, node * 2, left, right)
    rsum = query(mid + 1, end, node * 2 + 1, left, right)
    return lsum + rsum

ans = 0

for key in temp_A:
    ans += query(0, N-1, 1, B[key] + 1, N-1)
    update(0, N-1, 1, B[key])
    
print(ans)