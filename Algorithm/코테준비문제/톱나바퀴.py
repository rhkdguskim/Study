# https://www.acmicpc.net/problem/14891
move = (1, -1)
north = 0
right = 2
left = 6

def sumScore(graph):
    sum = 0
    for i in range(1, len(graph)):
        if graph[i][north] == '1':
            sum += (2)**(i-1)
            
    return sum 

def rightRotate(arr): # 시계방향
    temp = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        arr[i+1] = arr[i]
    
    arr[0] = temp
    
def leftRotate(arr): # 반시계
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
        
    arr[-1] = temp

def dfs(node, direction):
    visited[node] = True
    for d in move:
        newnode = d + node
        if 4 >= newnode >= 1 and not visited[newnode]:
            # 극이 다르다면
            if node > newnode: # 좌측 톱니바퀴 인경우
                if graph[node][left] != graph[newnode][right]:
                    dfs(newnode, -direction)
            else: # 우측 톱니바퀴인경우
                if graph[node][right] != graph[newnode][left]:
                    dfs(newnode, -direction)
                    
    if direction == 1: # 시계방향
        rightRotate(graph[node])
    else: # 반시계 방향
        leftRotate(graph[node])


graph = [[] for _ in range(5)]

for i in range(1, 5):
    graph[i] = list(input())
    
K = int(input())
for _ in range(K):
    visited = [False for _ in range(5)]
    node, dir = map(int, input().split())
    dfs(node, dir)

print(sumScore(graph))