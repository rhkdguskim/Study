# https://www.acmicpc.net/problem/1182
import sys
input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
def solve(queue, idx):
    global cnt
    if queue:
        if sum(queue) == S:
            cnt += 1

    for i in range(idx, N):
        queue.append(arr[i])
        solve(queue, i+1)
        queue.pop()

solve([], 0)
print(cnt)
