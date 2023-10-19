import math
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
treesize = int(pow(2,(math.ceil(math.log2(N)))+1))
tree = [[0 for _ in range(2)] for _ in range(treesize)] # 최대값과 최소값을 담을 배열
INF = int(1e10)

arr = [0 for _ in range(N+1)]
for i in range(1,N+1):
    arr[i] = int(input())

def init(node, start, end):
    if start == end: # leaf 노드에 달햇을경우
        tree[node][0] = arr[end]
        tree[node][1] = arr[end]
        return tree[node]

    mid = (start + end) // 2
    leftval = init(node*2, start, mid)
    rightval = init(node*2+1, mid+1, end)
    tree[node][0] = min(leftval[0], rightval[0])
    tree[node][1] = max(leftval[1], rightval[1])
    return tree[node]

def query(node, start, end, left, right):
    if right < start or left > end: # 범위가 벗어난경우
        return [INF, -INF]

    if left <= start and right >= end: # 범위에 있는경우
        return tree[node]

    mid = (start + end) // 2
    leftval = query(node*2, start, mid, left, right)
    rightval = query(node*2+1, mid+1, end, left, right)
    return [min(leftval[0],rightval[0]), max(leftval[1], rightval[1])]

init(1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())
    result = query(1, 1, N, a, b)
    print(result[0], result[1])
