# https://www.acmicpc.net/problem/6549
# 최소 높이와 left와 right의 크기를 알면 직사각형의 넓이를 저장 할 수 있다.
import sys
input = sys.stdin.readline
INF = int(1e9) + 1
sys.setrecursionlimit(int(1e5))

def merge(left, right):
    if left[0] > right[0]:
        return right
    else:
        return left

def init(start, end, node):
    if start == end:
        tree[node][0] = temp[start]
        tree[node][1] = start
        return tree[node]
    else:
        mid = (start + end) // 2
        l_init = init(start, mid, node*2)
        r_init = init(mid + 1, end, node*2+1)
        tree[node] = merge(l_init, r_init)
        return tree[node]
    
def query(start, end, node, left, right):
    if left > end or right < start:
        return [INF, 0]
    
    if start >= left and end <= right:
        return tree[node]
    
    mid = ( start + end ) // 2
    l_min = query(start, mid, node * 2, left, right)
    r_min = query(mid + 1, end, node * 2 + 1, left, right)
    return merge(l_min, r_min)
    
def solve(start, end):
    if start == end:
        return temp[start]
    if start > end:
        return -1
    
    height, idx = query(0, arr_size-1, 1, start, end)
    
    a = solve(start, idx - 1)
    b = solve(idx + 1, end)
    c = height * ((end - start) + 1)
    return max(a, b, c)
        
while True:
    temp = list(map(int, input().split()))
    arr_size = temp.pop(0)
    if arr_size == 0:
        break
    
    tree_size = arr_size * 4
    tree = [[0,0] for _ in range(tree_size)]
    init(0, arr_size-1, 1)
    print(solve(0, arr_size-1))
    