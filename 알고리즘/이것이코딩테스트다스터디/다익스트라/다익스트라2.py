start = 1
n = 6
m = 11
grahp = [[] for _ in range(n+1)]
INF = 10e9
for i in range(0, m):
    a,b,c = (map(int,input().split())) # start end 간선길이로 입력받는다.
    grahp[a].append([b,c]) # ex) 1번 노드는 2번노드와 4의 길이로 연결되어있다.
    
visited = [False] * (n+1)
distance = [INF] * (n+1)

def findminIndex() :
    mindata = INF
    idx = 0
    for i in range(1, n + 1):
        if(distance[i] < mindata and visited[i] == False):
            mindata = distance[i]
            idx = i
    
    return idx
        
def dikstra(start):
    visited[start] = True # 자기자신을 방문 한다
    distance[start] = 0
    for i in grahp[start]: # 관련된 노드들을 업데이트한다
        a, b = i
        distance[a] = b + distance[start]
        
    #이제 하나씩 방문하면 된다.
    for i in range(n-1):
        new = findminIndex()
        visited[new] = True # 자기자신을 방문 한다
        for j in grahp[new]: # 관련된 노드들을 업데이트한다
            cost = distance[new] + j[1]
            if(cost < distance[j[0]]):
                distance[j[0]] = cost
                
for i in range(1, n+1):
    if (distance[i] == INF):
        print("도달할 수 없음")
    else :
        print(distance[i])
        
        

    
    
    
