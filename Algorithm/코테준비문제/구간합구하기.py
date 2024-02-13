import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

tree = [0 for _ in range(N+1)]
arr = [0 for _ in range(N+1)]

def prefixSum(i):
    sum = 0
    while i:
        sum += tree[i]
        i -= (i & -i)
        
    return sum

def sumInterval(start, end):
    return prefixSum(end) - prefixSum(start - 1)

def update(num, idx):
    while N >= idx:
        tree[idx] += num
        idx += (idx & -idx)

for i in range(1, N+1):
    num = int(input())
    arr[i] = num
    update(num, i)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(c - arr[b], b)
        arr[b] = c
    else:
        print(sumInterval(b,c))