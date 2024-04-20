# https://www.acmicpc.net/problem/10868
import sys
input = sys.stdin.readline
INF = int(1e9) + 1

N, M = map(int, input().split())

data = [int(input()) for _ in range(N)]

tree = [[0, 0] for _ in range(4*N)]

def init(start, end, node):
    if start == end:
        tree[node][0] = data[start]
        tree[node][1] = data[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        lvalue = init(start, mid, node * 2)
        rvalue = init(mid+1, end, node * 2 + 1)
        tree[node][0] = min(lvalue[0], rvalue[0])
        tree[node][1] = max(lvalue[1], rvalue[1])
        return tree[node]
    
def query(start, end, node, left, right):
    if right < start or left > end:
        return [INF, -INF]
    
    if start >= left and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    lquery = query(start, mid, node*2, left, right)
    rquery = query(mid+1, end, node*2+1, left, right)
    return [min(lquery[0], rquery[0]), max(lquery[1], rquery[1])]

init(0, N-1, 1)

for _ in range(M):
    a, b = map(int, input().split())
    result = query(0, N-1, 1, a-1, b-1)
    print(result[0])