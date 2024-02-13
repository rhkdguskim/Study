import math
import sys
input = sys.stdin.readline
INF = int(1e10)

N, M = map(int, input().split())
arr = [0 for _ in range(N+1)]
treesize = int(pow(2,(math.ceil(math.log2(N)))+1))
tree = [INF for _ in range(treesize)]

def init(node, start, end):
    if start == end: # leaf node
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    tree[node] = min(init(node*2, start, mid), init(node*2+1, mid+1, end))
    return tree[node]

def query(node, start, end, left, right):
    if right < start or left > end: # 범위 이상인경우
        return INF

    if left <= start and right >= end: # 범위 안에 있는경우
        return tree[node]

    # 범위가 걸쳐서 있는경우
    mid = (start + end) // 2
    leftmin = query(node*2, start, mid, left, right)
    rightmin = query(node*2+1, mid+1, end, left, right)
    return min(leftmin, rightmin)

def update(node, start, end, idx, diff):
    if start == end: # leaf node
        tree[node] += diff
        return

    mid = (start + end) // 2
    if start <= idx <= mid:
        return update(node*2, start, mid, idx, diff)
    else:
        return update(node*2+1, mid +1, start, idx, diff)

for i in range(1, N+1):
    arr[i] = int(input())


init(1, 1, N)
for _ in range(M):
    a, b = map(int, input().split())
    print(query(1, 1, N, a, b))