# https://school.programmers.co.kr/learn/courses/30/lessons/60061

# [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# x, y, (기둥, 보), (삭제, 설치)
from copy import deepcopy

def solution(n, build_frame):
    EMPTY = -1
    PILLOW = 0
    BOW = 1
    graph = [[[EMPTY, EMPTY] for _ in range(n+1)] for _ in range(n+1)]
    
    def install(x, y, type):
        if type == PILLOW:
            if y == 0 or (graph[y][x][PILLOW] == PILLOW or graph[y][x][BOW] == BOW):
                graph[y][x][type] = type
                graph[y+1][x][type] = type
                print(x, y, type)
        else:
            if (graph[y][x][PILLOW] == PILLOW or graph[y][x+1][PILLOW] == PILLOW) or (graph[y][x][BOW] == BOW and graph[y][x+1][BOW] == BOW):
                graph[y][x][type] = type
                graph[y][x+1][type] = type
                print(x, y, type)
            
    
    for x, y, type, op in build_frame:
        if op == 1:
            install(x, y, type)
        else:
            pass
    
    # for s in reversed(graph):
    #     print(s)
    
    answer = [[]]
    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))