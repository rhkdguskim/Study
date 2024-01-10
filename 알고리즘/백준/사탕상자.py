# https://www.acmicpc.net/problem/2243
import sys
input = sys.stdin.readline
CANDY_CNT = 1000001

N = int(input())
# candy = [0 for _ in range(CANDY_CNT)]
tree = [[0, 0] for _ in range(CANDY_CNT * 4)]

def update(start, end, node, idx, value):
    if start > idx or end < idx:
        return
    
    if start == end:
        tree[node][0] += value
        if not tree[node][0]:
            tree[node][1] = 0
        else:
            tree[node][1] = idx
        return
        
    mid = ( start + end ) // 2
    update(start, mid, node*2, idx, value)
    update(mid+1, end, node*2+1, idx, value)
    tree[node][0] = tree[node*2][0] + tree[node*2+1][0]
    tree[node][1] = max(tree[node*2][1], tree[node*2+1][1])


def query(start, end, node, cnt):
    if start == end:
        return tree[node]
    else:
        mid = ( start + end ) // 2
        l_q = query(start, mid, node*2, cnt)
        
        if l_q[0] >= cnt:
            return l_q
        else:
            return query(mid+1, end, node*2+1, cnt)
    

for _ in range(N):
    temp = list(map(int, input().split()))
    if temp[0] == 2:
        B, C = temp[1:]
        update(1, CANDY_CNT, 1, B, C)
        # candy[B] += C
    else:
        B = temp[-1]
        r = query(1, CANDY_CNT, 1, B)
        update(1, CANDY_CNT, 1, r[1], -1)
        # candy[r[1]] -= 1
        print(r[1])
    
    #print("candy", candy[:10])

