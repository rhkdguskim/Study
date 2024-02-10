# https://www.acmicpc.net/problem/7453
import sys
input = sys.stdin.readline

N = int(input())
A = []
B = []
C = []
D = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
AB = []
CD = []
for i in range(N):
    for j in range(N):
        AB.append((A[i]+B[j]))
        CD.append((C[i]+D[j]))
        
pleft = 0
pright = len(CD) - 1
AB.sort()
CD.sort()
ans = 0

def find_cnt(value, arr):
    start = 0
    end = len(arr)-1
    left_idx = -1
    
    while end >= start:
        mid = (start + end) // 2
        if arr[mid] > value:
            end = mid - 1
        else:
            left_idx = mid
            start = mid + 1
    
    start = 0
    end = N*N-1
    right_idx = -1
    while end >= start:
        mid = (start + end) // 2
        if arr[mid] >= value:
            right_idx = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return right_idx - left_idx + 1

while pleft < len(AB) and 0 <= pright:
    cost = AB[pleft] + CD[pright]
    if cost == 0:
        check_left = AB[pleft]
        check_right = CD[pright]
        left_cnt = 0
        right_cnt = 0
        while pleft < len(AB) and AB[pleft] == check_left:
            left_cnt += 1
            pleft += 1
            
        while 0 <= pright and CD[pright] == check_right:
            right_cnt += 1
            pright -= 1
        
        ans += left_cnt * right_cnt
        
    elif cost > 0:
        pright -= 1
    else:
        pleft += 1
        
print(ans)