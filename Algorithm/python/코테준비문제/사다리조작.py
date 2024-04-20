# https://www.acmicpc.net/problem/15684
import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
sa = [[False for _ in range(H+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    sa[b][a] = True # b, b+1의 세로선을 높이 a의 위치에서 연결함.

def solution(depth, x,y):
    if check():
        return depth

    if depth >= 3:
        return depth + 1

    ans = 4
    for h in range(x, H+1):
        if h == x:
            k = y  # 행이 변경되기 전에는 가로선을 계속해서 탐색
        else:
            k = 1  # 행이 변경될 경우 가로선 처음부터 탐색
        for c in range(k, N):
            if not sa[c][h] and not sa[c-1][h] and not sa[c+1][h]: # 현재위치에서 사다리가 연결되어있지 않다면
                sa[c][h] = True
                ans = min(solution(depth+1, h, c+2), ans)
                sa[c][h] = False

    return ans

def check():
    for i in range(1, N+1):
        h = 1
        cur = i
        while H >= h:
            if sa[cur][h] or sa[cur-1][h]:
                if sa[cur][h]:
                    cur += 1
                else:
                    cur -= 1

            h += 1
        if cur != i:
            return False

    return True

answer = solution(0,1, 1)
if answer == 4:
    print(-1)
else:
    print(answer)