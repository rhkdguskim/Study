# https://school.programmers.co.kr/learn/courses/30/lessons/60061

# [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# x, y, (기둥, 보), (삭제, 설치)
def solution(n, build_frame):
    EMPTY = -1
    PILLOW = 0
    BOW = 1
    graph = [[[EMPTY, EMPTY] for _ in range(n+1)] for _ in range(n+1)]
    
    def install(x, y, type):
        if type == PILLOW:
            # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
            if y == 0 or (graph[y][x][PILLOW] == PILLOW or graph[y][x][BOW] == BOW):
                graph[y][x][type] = type
                graph[y+1][x][type] = type
                #print(x, y, type)
        else:
            # 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
            if (graph[y][x][PILLOW] == PILLOW or graph[y][x+1][PILLOW] == PILLOW) or (graph[y][x][BOW] == BOW and graph[y][x+1][BOW] == BOW):
                graph[y][x][type] = type
                graph[y][x+1][type] = type
                #print(x, y, type)
    
    def remove(x, y, type):
        # y에 (x+1), (x-1)에 bow가 있거나 x에 pillow가 있는경우만 삭제가능
        if type == PILLOW:
            pass
    
    for x, y, type, op in build_frame:
        if op == 1:
            install(x, y, type)
        else:
            pass
    
    # for s in reversed(graph):
    #     print(s)
    
    answer = [[]]
    return answer

#print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))