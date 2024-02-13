# https://www.acmicpc.net/problem/5676
import sys

input = sys.stdin.readline

def update(node, value, dif):
    def execute(node, tree, dif):
        while node <= N:
            tree[node] += dif
            node += (node & -node)
        
    if value < 0:
        execute(node, minus_fwt, dif)
    elif value == 0:
        execute(node, zero_fwt, dif)
        
def query_cnt(node, tree):
    cnt = 0
    while node >= 1:
        cnt += tree[node]
        node -= (node & -node)

    return cnt

while True:
    try:
        N, K = map(int, input().split())
        arr = list(map(int, input().split()))
        minus_fwt = [0] * (N+1)
        zero_fwt = [0] * (N+1)
        
        for i in range(1, N+1):
            update(i, arr[i-1], 1)
                
        ans = []
        for _ in range(K):
            temp = list(map(str, input().split()))
            if temp[0] == 'C':
                a, b = map(int, temp[1:])
                update(a, arr[a-1], -1)
                update(a, b, 1)
                arr[a-1] = b
            else:
                a, b = map(int, temp[1:])
                a = a-1
                if query_cnt(b, zero_fwt) - query_cnt(a, zero_fwt) > 0:
                    ans.append('0')
                    continue
                
                minus_cnt = query_cnt(b, minus_fwt) - query_cnt(a, minus_fwt)
                
                if minus_cnt % 2 == 0:
                    ans.append('+')
                else:
                    ans.append('-')
                
        print(''.join(ans))
    except Exception as e:
        #print(f"An exception occurred: {e}")
        break