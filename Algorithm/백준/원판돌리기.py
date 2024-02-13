# https://www.acmicpc.net/problem/17822
import sys
from collections import deque
input = sys.stdin.readline

CONVERSE = 0 # 시계방향
REVERSE = 1 # 반시계 방향

move = [(1,0), (-1,0), (0,-1), (0, 1)] 
# 예외사항이 있다.
# i가 0보다 작을때에는 무시 한다.
# j가 0보다 작다면 마지막 원소를 가르키도록 한다.
# j가 M이랑 같아진다면 첫번째 원소를 가르키도록 한다.

N, M, T = map(int, input().split())

graph = [deque(map(int, input().split())) for _ in range(N)]

def rotate(size, dir, k):
    # 시계 방향이라면
    for _ in range(k):
        if dir == CONVERSE:
            # 마지막원소를 첫번째에 넣는다.
            num = graph[size].pop()
            graph[size].appendleft(num)
        #  반시계 방향이라면
        else:
            # 첫번째원소를 마지막에 넣는다.
            num = graph[size].popleft()
            graph[size].append(num)
        
def find_near():
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited_flag = False
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] > 0:
                num = graph[i][j]
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                flag = False
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in move:
                        ny, nx = dy + y, dx + x
                        if N > ny >= 0 and M >= nx >= -1:
                            # 예외사항
                            if nx == -1: nx = M-1
                            elif nx == M: nx = 0
                            if not visited[ny][nx] and graph[ny][nx] == num:
                                visited[ny][nx] = True
                                visited_flag = True
                                flag = True
                                queue.append((ny, nx))
                                graph[ny][nx] = 0 # 모든 수를 0으로 바꾼다.
                                
                if flag: # 만약 같은 수가 하나라도 있다면 자기 자신도 바꾼다.
                    graph[i][j] = 0
    
    return visited_flag

def average_change():
    total = 0
    cnt  = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                total += graph[i][j]
                cnt += 1
    if cnt > 0:
        average = total / cnt
        for i in range(N):
            for j in range(M):
                if graph[i][j] > 0:
                    if graph[i][j] > average:
                        graph[i][j] -= 1
                    elif graph[i][j] < average:
                        graph[i][j] += 1

for _ in range(T):
    x, d, k = map(int, input().split())
    for t in range(x, N+1, x):
        rotate(t-1, d, k)
        
    # for g in graph:
    #     print(g)
        
    if not find_near():
        #print("평균 계산해버리기")
        average_change()
    
    #print("-------")
    # for g in graph:
    #     print(g)

ans = 0
for i in range(N):
    ans += sum(graph[i])
    
print(ans)