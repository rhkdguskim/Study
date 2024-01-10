# https://www.acmicpc.net/problem/2243
import sys
input = sys.stdin.readline
CANDY_CNT = 1000001

N = int(input())
tree = [0 for _ in range(CANDY_CNT*4)]

def update(start, end, node, idx, value):
    if idx < start or idx > end:
        return
    
    if start == end:
        tree[node] += value
        return
    
    mid = (start+end)//2
    update(start, mid, node*2, idx, value)
    update(mid+1, end, node*2+1, idx, value)
    
    tree[node] = tree[node*2] + tree[node*2+1]
    
def query(start, end, node, cnt):
    if start == end:
        return end
    
    mid = (start+end)//2
    cur_cnt = tree[node*2]
    if cur_cnt >= cnt:
        return query(start, mid, node*2, cnt)
    else:
        return query(mid+1, end, node*2+1, cnt - cur_cnt) 
    

for _ in range(N):
    temp = list(map(int, input().split()))
    if temp[0] == 2:
        B, C = temp[1:]
        update(0, CANDY_CNT, 1, B, C)
    else:
        B = temp[-1]
        candy = query(0, CANDY_CNT, 1, B)
        print(candy)
        update(0, CANDY_CNT, 1, candy, -1)