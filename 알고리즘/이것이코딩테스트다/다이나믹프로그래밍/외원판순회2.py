N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int ,input().split())))

INF = int(1e9)
dp = [[None] * (1 << N) for _ in range(N)] # N을 좌 shfit 하면 N*2 가 된다.
def dfs(i, visited):
    if visited == (1 << N) -1: # 모든 도시를 다 방문 했다면 (비트 의 전체합 -1 이면 모두 방문한 상황)
        if graph[i][0]:
            return graph[i][0] # 출발점으로 가는 경로가 있다면 출발점으로 가는 경로 출력
        else:
            return INF # 출발점으로 가는 경로가 없다면 INF 출력
        
    if dp[i][visited] != None: # 이미 최소비용이 계산되어있다면 출력
        return dp[i][visited]
    
    temp = INF
    for x in range(1, N):
        if not graph[i][x] or visited & (1 << x): # 가는 경로가 없거나 이미 방문한 도시라면 skip
            continue
        
        temp = min(temp, dfs(x, visited | (1 << x)) + graph[i][x]) # i가 4일경우 10000 값을 or 연산한다.
        
    dp[i][visited] = temp
    return temp
            
print(dfs(0,1))