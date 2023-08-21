# https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(100001)
T = int(input())


def dfs(student):
    global result
    visited[student] = True
    cycle.append(student)
    newstudent = graph[student]
    
    if visited[newstudent]:
        if newstudent in cycle:
            result += cycle[cycle.index(newstudent):] # 자기자신으로부터 마지막팀원까지 그룹핑
        return
    else:
        dfs(newstudent)

for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split()))
    result = []
    visited = [False for _ in range(n+1)]
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)    
            
    print(n - len(result))