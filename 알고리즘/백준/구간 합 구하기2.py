# https://www.acmicpc.net/problem/10999
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

tree_size = 4 * N

arr = [int(input()) for _ in range(N)]

tree = [0 for _ in range(tree_size)]
lazy = [0 for _ in range(tree_size)]

def init(start, end, node):
    if start == end:
        tree[node] += arr[start]
    else:
        mid = (start + end) // 2
        init(start, mid, node * 2)
        init(mid+1, end, node * 2 + 1)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]

def update_lazy(start, end, node):
    if lazy[node] != 0:
        tree[node] += lazy[node] * (end - start + 1)
        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]
        lazy[node] = 0
    
def update(start, end, left, right, node, diff):
    update_lazy(start, end, node)
    if left > end or right < start:
        return
    
    if start >= left and end <= right:
        tree[node] += (end - start + 1) * diff
        if start != end:
            lazy[node * 2] += diff
            lazy[node * 2 + 1] += diff
        return
    mid = ( start + end ) // 2
    update(start, mid, left, right, node * 2, diff)
    update(mid + 1, end, left, right, node * 2 + 1, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    
def query(start, end, left, right, node):
    update_lazy(start, end, node)
    if left > end or right < start:
        return 0
    if start >= left and end <= right:
        return tree[node]
    mid = ( start + end ) // 2
    lquery = query(start, mid, left, right, node * 2)
    rquery = query(mid + 1, end, left, right, node * 2 + 1)
    return lquery + rquery
    

init(0, N-1, 1)

for _ in range(M+K):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        b, c, d = temp[1:]
        update(0, N-1, b-1, c-1, 1, d)
    else:
        b, c = temp[1:]
        print(query(0, N-1, b-1, c-1, 1))
            