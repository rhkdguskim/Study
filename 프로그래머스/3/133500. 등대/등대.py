import sys
sys.setrecursionlimit(10 ** 6)

graph = []
answer = 0
light = []

def dfs(node, parent):
    global answer
    global light

    for child in graph[node]:

        if child == parent:
            continue

        dfs(child, node)

        if light[child] == False and light[node] == False:
            light[node] = True
            answer += 1

def solution(n, lighthouse):
    global graph
    global light

    graph = [[] for i in range(n)]

    for light in lighthouse:

        a = light[0] - 1
        b = light[1] - 1

        graph[a].append(b)
        graph[b].append(a)

    light = [False] * n 

    dfs(0, 0)

    return answer