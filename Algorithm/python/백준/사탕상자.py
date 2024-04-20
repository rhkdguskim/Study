# https://www.acmicpc.net/problem/2243
import sys
input = sys.stdin.readline
CANDY_CNT = 1000001

N = int(input())
fwt = [0 for _ in range(CANDY_CNT+1)]

def update(candy, cnt):
    idx = candy
    while idx <= CANDY_CNT:
        fwt[idx] += cnt
        idx += (idx&-idx)

def query(idx):
    cnt = 0
    while idx >= 1:
        cnt += fwt[idx]
        idx -= (idx&-idx)
    
    return cnt

def find(cnt):
    start = 1
    end = CANDY_CNT
    while start < end:
        mid = (start+end) // 2
        rank = query(mid)
        if rank >= cnt:
            end = mid
        else:
            start = mid + 1
    return end

for _ in range(N):
    temp = list(map(int, input().split()))
    if temp[0] == 2:
        B, C = temp[1:]
        update(B, C)
    else:
        B = temp[-1]
        candy = find(B)
        print(candy)
        update(candy, -1)