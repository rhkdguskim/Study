# https://www.acmicpc.net/problem/1027
import sys

si = sys.stdin.readline

N = int(si())
arr = list(map(int, si().split()))

ans = 0
for i in range(N): # 가능한 모든 빌딩을 가본다.

    # 오른쪽으로가본다.
    rbuilding = []
    start = i+1
    while N > start:
        if rbuilding:
            incline = rbuilding[-1]
            dy, dx = arr[start] - arr[i], start - i
            if dy / dx > incline:
                rbuilding.append(dy / dx)
        else:
            dy, dx = arr[start] - arr[i], start - i
            rbuilding.append(dy / dx)

        start += 1

    # 왼쪽으로 가본다.
    lbuilding = []
    start = i-1
    while start > -1:
        if lbuilding:
            incline = lbuilding[-1]
            dy, dx = arr[start] - arr[i], start - i
            if dy / dx < incline:
                lbuilding.append(dy / dx)
        else:
            dy, dx = arr[start] - arr[i], start - i
            lbuilding.append(dy / dx)

        start -= 1
    #print(i, len(rbuilding), len(lbuilding))
    ans = max(ans, len(rbuilding) + len(lbuilding))

print(ans)