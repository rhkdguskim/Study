# https://school.programmers.co.kr/learn/courses/30/lessons/133500?language=python3

# 진입차수가 가장 많은 노드를 방문한다. ( ++ )
# child node들을 다방문한다.
# 남은 노드중에 진입차수가 그다음으로 큰 노드를 방문한다. ( ++ )
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

#print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
#print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))