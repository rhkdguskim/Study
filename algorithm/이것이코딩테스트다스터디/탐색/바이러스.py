# 신종 바이러스인 웜바이러스는 네트워크를 통해 전파된다.
# 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어있는 모든 컴퓨터는 웜 바이러스에 걸리게된다.
# 에를들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 사에서 연결되어있다고하자 1번 이 바이러스가 걸리면 2,5,3,6번까지 전파되어 바이러스 걸린다.
# 4번과 7번은 영향을 받지 않는다.
# 1번 바이러스를통하여 걸리게 되는 컴퓨터 수를 구하여라
# 깊이우선, 너비우선 탐색 둘다 가능
from collections import deque
N = int(input()) # 컴퓨터 수 (노드)
M = int(input()) # 쌍의 수 (간선)

graph = [list() for _ in range(N + 1)]
for i in range(M) :
    data = list(map(int, input().split()))
    graph[data[0]].append(data[1])
    graph[data[1]].append(data[0])

visited = [False] * (N + 1)

def bfs(start):
    counter = 0
    queue = deque([start])
    visited[start] = True
    while queue :
        newdata = queue.popleft()
        for n in graph[newdata]:
            if(visited[n] == False):
                queue.append(n)
                visited[n] = True
                counter += 1
    return counter
                
print(bfs(1))
