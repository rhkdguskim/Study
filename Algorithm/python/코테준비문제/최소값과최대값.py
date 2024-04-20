#https://www.acmicpc.net/problem/2357
import math
import sys
sys.setrecursionlimit(10000001)
input = sys.stdin.readline
INF = int(1000000001)
N, M = map(int, input().split())
H = math.ceil(math.log2(N))

def init(start,end, node):
    if start < 1 or end > N:
        return INF, 0
    
    if start == end:
        tree[node][0] = arr[start]
        tree[node][1] = arr[end]
        return tree[node][0], tree[node][1]
    
    mid = (start+end) // 2
    leftmin, leftmax = init(start, mid, node*2)
    rightmin, rightmax = init(mid+1, end, node*2+1)
    tree[node][0] = min(leftmin, rightmin)
    tree[node][1] = max(rightmax, leftmax)
    return tree[node][0], tree[node][1]
    
def find(start, end, left, right, node):
    if left > end or right < start: # 범위를 벗어난경우
        return INF, 0
    if left <= start and right >= end: # left,right가 start, end 범위에 있는경우
        return tree[node][0], tree[node][1]
    
    mid = (start + end ) // 2
    leftmin, leftmax = find(start, mid, left, right, node*2)
    rightmin, rightmax = find(mid+1, end, left, right, node*2+1)
    return min(leftmin, rightmin), max(leftmax, rightmax)


treesize = int(math.pow(2, H+1))

tree = [[INF,0] for _ in range(treesize)] # 최소값, 최대값
arr = [0 for _ in range(N+1)]

for i in range(1, N+1):
    arr[i] = int(input())
    
init(1, N, 1)

for _ in range(M):
    a, b = map(int, input().split())
    minvalue, maxvalue = find(1, N, a, b, 1)
    print(minvalue, maxvalue)