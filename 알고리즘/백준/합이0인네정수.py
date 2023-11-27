# https://www.acmicpc.net/problem/7453
import sys
input = sys.stdin.readline
N = int(input())
visited = set()

A = []
B = []
C = []
D = []
for _ in range(N):
    temp = list(map(int, input().split()))
    A.append(temp[0])
    B.append(temp[1])
    C.append(temp[2])
    D.append(temp[3])

A.sort()
B.sort()
C.sort()
D.sort()

ans = 0
def solve(a_s, a_e, b_s, b_e, c_s, c_e, d_s, d_e):
    global ans
    if a_s > a_e or b_s > b_e or c_s > c_e or d_s > d_e:
        return
    
    if (a_s, a_e, b_s, b_e, c_s, c_e, d_s, d_e) in visited:
        return
    
    # 방문처리
    visited.add((a_s, a_e, b_s, b_e, c_s, c_e, d_s, d_e))
    
    a_m = (a_s + a_e) // 2
    b_m = (b_s + b_e) // 2
    c_m = (c_s + c_e) // 2
    d_m = (d_s + d_e) // 2

    total = A[a_m] + B[b_m] + C[c_m] + D[d_m]
    if total > 0: # total이 더 클경우
        # 왼쪽을 탐색해본다.
        solve(a_s, a_m-1, b_s, b_e, c_s, c_e, d_s, d_e)
        solve(a_s, a_e, b_s, b_m-1, c_s, c_e, d_s, d_e)
        solve(a_s, a_e, b_s, b_e, c_s, c_m-1, d_s, d_e)
        solve(a_s, a_e, b_s, b_e, c_s, c_e, d_s, d_m-1)
    else:
        if total == 0:
            ans += 1
        # 오른쪽
        solve(a_m+1, a_e, b_s, b_e, c_s, c_e, d_s, d_e)
        solve(a_s, a_e, b_m+1, b_e, c_s, c_e, d_s, d_e)
        solve(a_s, a_e, b_s, b_e, c_m+1, c_e, d_s, d_e)
        solve(a_s, a_e, b_s, b_e, c_s, c_e, d_m+1, d_e)

solve(0, N-1, 0, N-1, 0, N-1, 0, N-1)
print(ans)