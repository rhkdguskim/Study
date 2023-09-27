# https://www.acmicpc.net/problem/11505
import sys
input = sys.stdin.readline
import math
N , M , K = map(int, input().split())
H = math.ceil(math.log2(N))

def init(start, end, node):
    if start < 1 or end > N:
        return 1
    
    if start == end:
        tree[node] *= arr[end]
        return tree[node]
    else:
        mid = (start + end ) // 2
        leftnode = init(start, mid, node*2)
        rightnode = init(mid + 1, end, node*2+1)
        tree[node] = leftnode * rightnode
        return tree[node]


def update(start,end, left, right, node, value):
    if left > end or right < start:
        return 1
    
    if left <= start and right >= end:
        tree[node] *= value
        return tree[node]
    
    
    mid = (start + end) // 2
    leftnode = update(start, mid, left, right, node *2, value)
    rightnode = update(mid + 1, end, left, right, node *2+1, value)
    tree[node] = leftnode * rightnode * value
    return tree[node]

def find(start,end, left, right, node):
    if left > end or right < start:
        return 1
    
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start + end) // 2
    leftnode = find(start, mid, left, right, node *2)
    rightnode = find(mid + 1, end, left, right, node *2+1)
    tree[node] = leftnode * rightnode
    return tree[node]
    
    
    
treesize = int(math.pow(2, H+1))
arr = [1 for _ in range(N+1)]
tree = [1 for _ in range(treesize)]


for i in range(1, N+1):
    arr[i] = int(input())

init(1, N, 1)
print(tree)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        print(arr)
        update(1, N, 1, b, 1, c//arr[b])
        arr[b] = c
        print(arr)
        print(tree)
        
    else:
        print("result:",find(1,N, a, b, 1))