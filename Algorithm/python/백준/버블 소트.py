# https://www.acmicpc.net/problem/1517
# 현재 idx에서 오른쪽 값에서 자기자신보다 작은개수가 swap 횟수이다.

import sys
input = sys.stdin.readline

N = int(input())

data = list(map(int, input().split()))

def init(start, end, node, value):
    if start == end:
        if value > data[end]:
            tree[node] = 1
        return tree[node]
    else:
        mid = ( start + end ) // 2
        tree[node] = init(start, mid, node*2, value) + init(mid+1, end, node*2+1, value)
        return tree[node]

def query(start, end, node, left, right):
    if left > end or right < start:
        return 0
    
    if start >= left and end <= right:
        return tree[node]
    
    mid = ( start + end ) // 2
    return query(start, mid, node*2, left, right) +  query(mid + 1, end, node*2+1, left, right)
        
ans = 0
for i in range(N):
    tree = [0 for _ in range(4 * N)]
    init(0, N-1, 1, data[i])
    cnt = query(0, N-1, 1, i+1, N-1)
    ans += cnt
        
print(ans)