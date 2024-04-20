# https://www.acmicpc.net/problem/2042
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0 for _ in range(4*N)]

def init(start, end, node):
    if start == end:
        tree[node] += arr[start]
    else:
        mid = (start + end) // 2
        init(start, mid, node * 2)
        init(mid + 1, end, node * 2 + 1)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]
        
def update(start, end, node, idx, diff):
    if idx < start or end < idx:
        return
    
    if start == end:
        tree[node] += diff
        return
    
    mid = (start + end) // 2
    update(start, mid, node * 2, idx, diff)
    update(mid + 1, end, node * 2 + 1, idx, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    
def query(start, end, left, right, node):
    if right < start or left > end:
        return 0
    
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start + end) // 2
    lsum = query(start, mid, left, right, node * 2)
    rsum = query(mid + 1, end, left, right, node * 2 + 1)
    return lsum + rsum
    
init(0, N-1, 1)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b-1]
        update(0, N-1, 1, b-1, diff)
        arr[b-1] = c
    else:
        print(query(0, N-1, b-1, c-1, 1))