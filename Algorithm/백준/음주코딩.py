# https://www.acmicpc.net/problem/5676
import sys
import math

input = sys.stdin.readline

def parse(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0

def init(start, end, node):
    if start == end:
        tree[node] = parse(arr[start])
    else:
        mid = (start + end) // 2
        tree[node] = init(start, mid, 2*node) * init(mid+1, end, 2*node + 1)
    return tree[node]
 
def query(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
 
    mid = (start + end) // 2
    return query(start, mid, 2*node, left, right) * query(mid+1, end, 2*node + 1, left, right)
 
def update(start, end, node, where, diff):
    if where < start or end < where:
        return
 
    if start == end:
        tree[node] = parse(diff)
    else:
        mid = (start + end) // 2
        update(start, mid, node*2, where, diff)
        update(mid+1, end, node*2 + 1, where, diff)
        tree[node] = tree[2*node] * tree[2*node + 1]
    
while True:
    try:
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        tree = [0] * (1 << (int(math.ceil(math.log2(N))) + 1))
        init(0, N-1, 1)
        ans = []
        for _ in range(K):
            temp = list(map(str, input().split()))
            if temp[0] == 'C':
                a, b = map(int, temp[1:])
                update(0, N-1, 1, a-1, b)
            else:
                a, b = map(int, temp[1:])
                temp = query(0, N-1, 1, a-1, b-1)
                if temp == 1:
                    ans.append('+')
                elif temp == -1:
                    ans.append('-')
                else:
                    ans.append('0')
                
        print(''.join(ans))
    except:
        break