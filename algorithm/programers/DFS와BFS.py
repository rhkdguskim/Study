from collections import deque

N, M, V = map(int, input().split()) # N: 정점의 개수, M:간선의 개수 , V:탐색시작정점
arr = []
for _ in range(M) : # 간선의 개수 만큼 정점 연결 정보를 입력받는다.
    arr.append(list(map(int, input().split())))

def makeGraph(N, M, arr):
    graph = list()
    for i in range(1, N+1): # 정점 배열 연결리스트 작성
        graph.append(list())
        for j in range(M): # 간선정보를 순회한다.
            if(i in arr[j]): # 간선에 자기자신이 포함되어있다면
                for data in arr[j]: # 해당 간선정보를 불러온다.
                    if(data != i and data not in graph[i - 1]): # 자기자신이 아닌값을 추가한다.
                        graph[i - 1].append(data)
    for i in range(len(graph)):
        graph[i].sort()
    return graph

visited = [False for _ in range(N)]
graph = makeGraph(N, M, arr)
def dfs(V):
    visited[V-1] = True
    print(V, end = " ")
    for data in graph[V-1]:
        if(visited[data - 1] == False): # 방문하지 않으면 방문한다.
            dfs(data)
            
visited2 = [False for _ in range(N)]          
def bfs(V):
    queue = deque()
    queue.append(V)
    visited2[V-1] = True
    print(V, end=" ")
        
    while queue:
        newdata = queue.popleft()
        for data in graph[newdata-1]:
            if(visited2[data-1] == False):
                queue.append(data)
                visited2[data-1] = True
                print(data, end=" ")
                  
dfs(V)
print()
bfs(V)