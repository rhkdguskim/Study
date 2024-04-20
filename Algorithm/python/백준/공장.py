# https://www.acmicpc.net/problem/7578
# 500,000 * 500, 000
# A의 구간 i부터 j까지 어떤 기계가 들어있는지 파악한다.
# B의 구간에 i부터 j 까지 어떤 기계가 들어있는지 파악한다.
import sys
input = sys.stdin.readline
N = int(input())

A = {}
B = {}

temp_A = list(map(int, input().split()))
temp_B = list(map(int, input().split()))

tree_A = [set() for _ in range(4*N)]
tree_B = [set() for _ in range(4*N)]

for i in range(N):
    A[temp_A[i]] = i
    B[temp_B[i]] = i

def init(start, end, node):
    if start == end:
        tree_A[node].add(temp_A[start])
        tree_B[node].add(temp_B[start])
    else:
        mid = ( start + end) // 2
        init(start, mid, node * 2)
        init(mid + 1, end, node * 2 + 1)
        tree_A[node] = tree_A[node*2] | tree_A[node*2+1]
        tree_B[node] = tree_B[node*2] | tree_B[node*2+1]
        
def query(start, end, left, right, node, tree):
    if left > end or right < start:
        return set()
    
    if start >= left and end <= right:
        return tree[node]
    
    mid = ( start + end) // 2
    l_search = query(start, mid, left, right, node * 2, tree)
    r_search = query(mid + 1, end, left, right, node * 2 + 1, tree)
    return l_search | r_search
    
init(0, N-1, 1)

ans = set()
for key in A:
    temp = query(0, N-1, 0, A[key]-1, 1, tree_A) & query(0, N-1, B[key]+1, N-1, 1, tree_B)
    temp2 = query(0, N-1, A[key]+1, N-1, 1, tree_A) & query(0, N-1, 0, B[key]-1, 1, tree_B)
    for t in temp:
        ans.add((key, t))
        ans.add((t, key))
        
    for t2 in temp2:
        ans.add((key, t2))
        ans.add((t2, key))

print(len(ans) // 2)