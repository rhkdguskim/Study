import math
import sys
input = sys.stdin.readline
N = int(input())
graph = [[0, 0] for _ in range(N+1)]
level = [[] for _ in range(int(math.ceil(math.log2(N))+1)+1)] # 트리의 높이
for _ in range(N):
    node, left, right = map(int, input().split())
    graph[node][0] = left
    graph[node][1] = right


cnt = 1
def solve(node, depth):
    global cnt
    left, right = graph[node]

    if left != -1:
        solve(left, depth + 1)

    level[depth].append((cnt, node))
    cnt += 1

    if right != -1:
        solve(right, depth + 1)

solve(1,1)


