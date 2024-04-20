# https://www.acmicpc.net/problem/2458
# 처음 진입차수가 0이면서 간선이 있는경우 순서를 알 수 있다.
# 위상정렬을 통하여 방문한 노드는 순서를 알 수 있다.
import sys
input = sys.stdin.readline

N, M = map(int,input().split())


arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    small, big = map(int,input().split())
    arr[big][small] = 1 


for k in range(1,N+1):
    for s in range(1,N+1):
        if k==s:
            continue
        for g in range(1,N+1):
            if g==s:
                continue
            cnt = 0
            if arr[k][s] and arr[g][k]:
                cnt = 1

            arr[g][s] = max(arr[g][s], cnt)


answer = 0
for i in range(1,N+1):
    scnt = sum(arr[i])
    rcnt = sum([1 if arr[j][i] else 0 for j in range(1,N+1)])
    if scnt + rcnt == N-1:
        answer += 1

print(answer)