# https://www.acmicpc.net/problem/11505
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]
tree = [1 for _ in range(4*N)]

def init(node, start, end):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    else:
        mid = (start+end)//2
        left = init(node*2, start, mid)
        right = init(node*2+1, mid+1, end)
        tree[node] = left * right % 1000000007
        return tree[node]

def update(node, start, end, idx, value):
    if idx >= start and idx <= end:
        if start == end:
            tree[node] = value
            return
        else:
            mid = (start+end)//2
            update(node*2, start, mid, idx, value)
            update(node*2+1, mid+1, end, idx, value)
            tree[node] = tree[node*2] * tree[node*2+1] % 1000000007
            return
    
def query(node, start, end, left, right):
    if left > end or right < start:
        return 1
    else:
        if left <= start and right >= end:
            return tree[node]
        else:
            mid = (start+end)//2
            l_value = query(node*2, start, mid, left, right)
            r_value = query(node*2+1, mid+1, end, left, right)
            return l_value * r_value % 1000000007
    
init(1, 0, N-1)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 0, N-1, b-1, c)
    else:
        print(query(1, 0, N-1, b-1, c-1) % 1000000007)