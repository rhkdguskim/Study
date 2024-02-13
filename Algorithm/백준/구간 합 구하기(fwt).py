# https://www.acmicpc.net/problem/2042
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
fwt = [0 for _ in range(N+1)]

def update(node, diff):
    while node <= N:
        fwt[node] += diff
        node += node & (-node)

def query(node):
    ans = 0
    while node >= 1:
        ans += fwt[node]
        node -= node & (-node)
    return ans

def prefix_sum(start, end):
    return query(end) - query(start - 1)

for i in range(1, N+1):
    update(i, arr[i-1])

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b-1]
        update(b, diff)
        arr[b-1] = c
    else:
        print(prefix_sum(b, c))