import sys
input = sys.stdin.readlines()
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정 

n, m = map(int, input().split())
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
grahp = [[] for i in range(n+1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a , b, c = map(int ,input().split())
    grahp[a].append((b,c))
    
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if(distance[i] < min_value and not visited[i]):
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in grahp[start]:
        distance[j[0]] = j[1]
        
    for i in range(n-1):
        now = get_smallest_node() # 현재위치에서 가장 작은 간선 으로 이동할수있는 노드 선택
        visited[now] = True
        for j in grahp[now]: # 선택받은 노드에서 간선정보를 업데이트한다 ( 이미 값이 있다면 값을 비교하여 작은값을 업데이트 한다 )
            cost = distance[now] = j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("도달 할 수 없음")
    else:
        print(distance)
