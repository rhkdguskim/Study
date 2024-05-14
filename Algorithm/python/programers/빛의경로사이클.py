# https://school.programmers.co.kr/learn/courses/30/lessons/86052

# 노드의 타입에따라서 방향을 변경해준다.
# 범위를 넘어서면 범위를 자동으로 바꾸어주어야한다.
# 자기가 출발한 방향으로 다시 출발한다면 사이클이 존재한다.

# 노드로부터 4방향을 모두 체크해야한다. (UP, DOWN, LEFT, RIGHT) (0, 1, 2, 3)
# 해당노드를 탐색하지않았다면 다음노드도 반드시 탐색하지 않았다.
# S 직진(변화없음), L 좌회전(반시계방향), R 우회전(시계방향)
import sys
sys.setrecursionlimit(500000)

def solution(grid):
    IN = 0
    OUT = 1
    # RIGHT, DOWN, LEFT, UP
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def chage_dir(dir, type):
        if type == 'S':
            pass
        elif type == 'L':
            dir -= 1
        elif type == 'R':
            dir += 1
        return dir % 4
    
    def change_pos(i, j):
        return [i % rows, j % cols]
    
    rows = len(grid)
    cols = len(grid[0])
    
    visited = [[set() for _ in range(cols)] for _ in range(rows)]
    
    def dfs(i, j, dir):
        visited[i][j].add((dir, OUT))
        ny, nx = change_pos(moves[dir][0] + i, moves[dir][1] + j)
        dir = chage_dir(dir, grid[ny][nx])
        
        if (dir, IN) in visited[ny][nx]:
            return 0
        
        visited[ny][nx].add((dir, IN))
        return dfs(ny, nx, dir) + 1
        
    answer = []
    for i in range(rows):
        for j in range(cols):
            for m in range(4):
                if (m, OUT) not in visited[i][j]:
                    answer.append(dfs(i, j, m))
    
    if answer:
        answer.sort()
        
    return answer