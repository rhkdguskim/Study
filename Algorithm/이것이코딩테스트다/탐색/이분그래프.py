# https://www.acmicpc.net/problem/1707
# 처음에는 서로소 집합 문제라고 생각을 했으나, 이분 그래프 자료구조를 이해한뒤 탐색문제 이다.
# 이분 그래프는 그래프 형태의 자료구조인데 정점을 2그룹으로 나눌 수 있으되 같은 그룹의 정점끼리는 간선으로 이어지지 않은 경우를 의미한다.

# 1) 그룹 A를 {1} 1로설정 너비우선 탐색을 한다. (2,3,4) 를 방문한다고 치면 그룹을 B {2,4,5}로 설정
# 2) 2,3,4를 너비우선탐색을 또 한다. 그러나 그룹 B끼리는 연결되서는 안된다. 2 -> 3으로 가는경우는 이분그래프가 아니므로 NO출력
#     2,3,4에서 가는 방향이 자기자신의 그룹을 방문하지않으면 그룹 A로 지정
# 3) 탐색을 모두 끝낸뒤 NO 출력이 되지 않았으면 YES 출력 하면됨.
from collections import deque

K = int(input()) # 테스트 케이스


for _ in range(K): # 테스트 케이스 만큼 반복
    V, E = map(int, input().split()) # 정점의 개수, 간선의 개수
    visisted = [False for _ in range(V+1)]
    graph = [[] for _ in range(V+1)] # 해당 정점에서 다른정점까지의 가는 경로 정보 저장 그래프
    for _ in range(E):
        start, end = map(int, input().split())
        graph[end].append(start)
        graph[start].append(end) # 1번 정점에서 2번정점으로 가는경우 graph[1]에 2의 정점정보 추가
    

        
    # 너비 우선 탐색
    isbinaryGraph = True
    for i in range(V+1):
        queue = []
        if not visisted[i]: # 그룹이 지정되어있지 않다면
            queue = deque([i])
            visisted[i] = 1
        while queue:
            x = queue.popleft() # 정점을 pop 한다.
            for v in graph[x]:
                if not visisted[v]:
                    queue.append(v)
                    visisted[v] = -1 * visisted[x] # 다른 그룹 생성
                elif visisted[v] == visisted[x]:
                    isbinaryGraph = False
                    break
    if isbinaryGraph:
        print("YES")
    else:
        print("NO")