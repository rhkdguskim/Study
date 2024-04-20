#https://www.acmicpc.net/problem/10868
# 해당문제는 세그먼트 트리로 문제를 해결 할 수 있다. ( 구간 최소값 구하기 )
import sys
import math
input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1000000001)
arr = [0 for _ in range(N+1)]
H = math.ceil(math.log2(N))
treesize = int(math.pow(2, H+1))
tree = [0 for _ in range(treesize)]
print(treesize)
def init(start,end, node):
    if 1 > start or end > N: # 범위를 벗어낫을경우
        return INF
    
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        lefmin = init(start, mid, node*2)
        rightmin = init(mid+1, end, node*2 +1)
        tree[node] = min(lefmin, rightmin)
        return tree[node]

def findmin(start,end, left, right, node):
    if left > end or start > right: # 범위를 잘 생각해보자.
        return INF
    
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start + end ) // 2
    
    leftmin = findmin(start, mid, left, right, node*2)
    rightmin = findmin(mid+1, end, left, right, node*2 +1)
    
    return min(leftmin, rightmin)

for i in range(1, N+1):
    arr[i] = int(input())

init(1, N, 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(findmin(1, N, a, b, 1))
    