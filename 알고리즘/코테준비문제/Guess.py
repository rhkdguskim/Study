# https://www.acmicpc.net/problem/1248
from copy import deepcopy
N = int(input())
temp = list(input())
S = [[None for _ in range(N+1)] for _ in range(N+1)]
cnt = 0
for i in range(1,N+1):
    for j in range(i, N+1):
        if temp[cnt] == '+':
            S[i][j] = 1
        elif temp[cnt] == '-':
            S[i][j] = -1
        else:
            S[i][j] = 0

        cnt += 1

foundFlag = False
ans = []
def dfs(queue):
    # 백트래킹 조건
    global foundFlag, ans
    if foundFlag:
        return

    l = len(queue)
    if queue:
        # 테이블에 있는 조건 백트래킹
        for i in range(l-1, 0, -1):
            temp = sum(queue[i - 1:l])
            if S[i][l] == 1 and temp < 0:
                return

            if S[i][l] == -1 and temp > 0:
                return

            if S[i][l] == 0 and temp != 0:
                return

    if l == N:
        ans = deepcopy(queue)
        foundFlag = True
        return

    for i in range(1, 11):
        queue.append(i * S[len(queue)+1][len(queue)+1])
        dfs(queue)
        queue.pop()

dfs([])
print(*ans)


