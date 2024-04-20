#https://www.acmicpc.net/problem/1135
import sys

input = sys.stdin.readline

N = int(input())
emp = list(map(int, input().split()))
node = [[] for _ in range(N)]
child_cnt = [0 for _ in range(N)]


def solve(x):
    global child_cnt
    child_node = []
    if len(node[x]) == 0:
        child_cnt[x] = 0
    else:
        for child in node[x]:
            solve(child)
            child_node.append(child_cnt[child])

        child_node.sort(reverse=True)
        child_node = [child_node[i] + i + 1 for i in range(len(child_node))]
        child_cnt[x] = max(child_node)


for i in range(1, len(emp)):
    node[emp[i]].append(i)

solve(0)
print(child_cnt[0])