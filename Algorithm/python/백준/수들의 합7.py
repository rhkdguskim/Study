# https://www.acmicpc.net/problem/2268
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = [0 for _ in range(N+1)]

tree_size = 4*N

tree = [0 for _ in range(tree_size+1)]

def sum(start, end, node, left, right):
    # 범위를 벗어난경우
    if start > right or left > end:
        return 0
    
    # 범위안에 있는경우
    if start >= left and right >= end:
        return tree[node]
    else:
        mid = (start+end) // 2
        l_sum = sum(start, mid, node*2, left, right)
        r_sum = sum(mid+1, end, node*2+1, left, right)
        return l_sum + r_sum

def update(start, end, node):
    # 인덱스의 범위를 벗어난경우
    if start > idx or idx > end:
        return
    # 범위안에 있는경우
    # leaf 노드에 도달한경우
    if start == end:
        tree[node] = value
    else:
        mid = (start+end) // 2
        update(start, mid, node*2)
        update(mid+1, end, node*2+1)
        # leaf 노드에 도달한후 값을 업데이트
        tree[node] = tree[node*2] + tree[node*2+1]
        
for _ in range(M):
    temp = list(map(int, input().split()))
    if temp[0] == 0:
        # 구간 합 구하기
        if temp[1] > temp[2]:
            temp[1], temp[2] = temp[2], temp[1]
        print(sum(1, N, 1, temp[1], temp[2]))
    else:
        # 값 업데이트 하기
        idx, value = temp[1], temp[2]
        update(1, N, 1)