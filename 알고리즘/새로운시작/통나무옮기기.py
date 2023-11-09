# https://www.acmicpc.net/problem/1938
import sys
from collections import deque

input = sys.stdin.readline

dir = ('U', 'D', 'L', 'R', 'T')
move = [(-1,0), (1,0), (0,-1), (0,1)]
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
TURN = 4

H = 0 # 가로방향
V = 1 # 세로방향
N = int(input())
graph = []
for _ in range(N):
    temp = input().strip()
    graph.append(temp)

def find(char):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == char:
                # 가로 방향일때
                if j-1 >= 0 and N > j+1 and graph[i][j-1] == char and graph[i][j+1] == char:
                    return i, j, H
                
                # 세로 방향일때
                if i-1 >= 0 and N > i+1 and graph[i-1][j] == char and graph[i+1][j] == char:
                    return i, j, V
                
start_y, start_x, start_dir = find('B')
end_y, end_x, end_dir = find('E')

def check(i, j, dir, t):
    if dir == H :
        if t == UP: # 방향이 수직방향이고 위로 갈수 있다면
            if i-1 >= 0 and graph[i-1][j] != '1': return True
            else: return False
        
        if t == DOWN:
            if N > i+1 and graph[i+1][j] != '1': return True
            else: return True
        
        if t == LEFT:
            if i-1 >= 0 and j-1 >= 0 and N > i+1 and graph[i][j-1] != '1' and graph[i+1][j-1] != '1' and graph[i-1][j-1] != '1': return True
            else: return False
            
        if t == RIGHT:
            if N > i+1 and N > j+1 and i-1 >= 0 and graph[i][j+1] != '1' and graph[i+1][j+1] != '1' and graph[i-1][j+1] != '1': return True
            else: return False
            
        if t == TURN:
            y = i - 1
            x = j - 1
            if N > y >=0 and N > x >= 0:
                for ny in range(3):
                    for nx in range(3):
                        if N > ny + y >=0 and N > nx + x >=0:
                            if graph[ny+y][nx+x] == '1':
                                return False
                        else:
                            return False
            else:
                return False
                    
            return True
    else:
        if t == LEFT: # 방향이 수평방향이고 왼쪽으로 움직인다면
            if j-1 >= 0 and graph[i][j-1] != '1': return True
            else: return False
        
        if t == RIGHT:
            if N > j+1 and graph[i][j+1] != '1': return True
            else: return True
        
        if t == UP:
            if i-1 >= 0 and j-1 >= 0 and N > j+1 and graph[i-1][j] != '1' and graph[i-1][j-1] != '1' and graph[i-1][j+1] != '1': return True
            else: return False
            
        if t == DOWN:
            if N > i+1 and N > j+1 and j-1 >=0 and graph[i+1][j] != '1' and graph[i+1][j-1] != '1' and graph[i+1][j+1] != '1': return True
            else: return False
            
        if t == TURN:
            y = i - 1
            x = j - 1
            if N > y >=0 and N > x >= 0:
                for ny in range(3):
                    for nx in range(3):
                        if N > ny + y >=0 and N > nx + x >=0:
                            if graph[ny+y][nx+x] == '1':
                                return False
                        else:
                            return False
            else:
                return False
                    
            return True 
        

queue = deque()
queue.append((start_y, start_x, start_dir, 0))
visited = [[[False for _ in range(N)] for _ in range(N)] for _ in range(2)]
ans = 2501
while queue:
    y, x, dir, cost = queue.popleft()
    for t in range(5):
        ny, nx = y, x
        if t != TURN:
            ny, nx = move[t][0] + y, move[t][1] + x
        
        newdir = dir
        if t == TURN:
                if dir == V:
                    newdir = H
                else:
                    newdir = V
        if N > ny >=0 and N > nx >=0 and not visited[newdir][ny][nx] and check(y, x, dir, t) and graph[ny][nx] == '0':
            newcost = cost + 1
            print(ny, nx , newdir, newcost)
            visited[newdir][ny][nx] = True
            queue.append((ny, nx, newdir, newcost))
            if ny == end_y and nx == end_x and end_dir == dir:
                ans = min(ans, newcost)
                           
if ans == 2501:
    print(0)
else:
    print(ans)
    