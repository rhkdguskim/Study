# https://www.acmicpc.net/problem/11505
import sys
DIV = 1000000007

input = sys.stdin.readline

N, M, K = map(int, input().split())


arr = [int(input()) for _ in range(N)]

tree = [0 for _ in range(4*N)]
zero_tree = [False for _ in range(4*N)]

def init(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        mid = ( start + end ) // 2
        tree[node] = init(start, mid, node * 2) * init(mid + 1, end, node * 2 + 1) % DIV
        return tree[node]

def query(start, end, node, left, right):
    if left > end or right < start:
        return 1
    
    if left <= start and right >= end:
        return tree[node]
    
    mid = ( start + end ) // 2
    
    lmul = query(start, mid, node * 2, left, right)
    rmul = query(mid + 1, end, node * 2 + 1, left, right)
    return lmul * rmul % DIV

def update(start, end, node, idx, diff):
    if idx < start or idx > end:
        return
    
    if start == end:
        tree[node] = diff
        return tree[node]
    
    mid = ( start + end ) // 2
    
    update(start, mid, node * 2, idx, diff)
    update(mid + 1, end, node * 2 + 1, idx, diff)
    tree[node] = tree[node*2] * tree[node*2+1] % DIV
    return tree[node]
    

init(0, N-1, 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, N-1, 1, b-1, c)
        arr[b-1] = c
    else:
        print(query(0, N-1, 1, b-1, c-1))