INF = int(10e9)

n = int(input())
m = int(input())
# 2차원 리스트(그래프를 만든다), 모든값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신에서 자기자신으로 가는 비용 초기화
for i in range(n+1):
    graph[i][i] = 0
    
# 간선의 정보를 입력받아 초기화
for _ in range(m):
    a, b ,c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 알고리즘을 실행
for i in range(n):
    for a in range(n):
        for b in range(n):
            if (i != a and 1 != b and a != b):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])
    