# https://www.acmicpc.net/problem/1516
# 최소값을 초기화하는 배열이 필요
# 건축시간을 갖고있는 배열이 필요

# 위상정렬을 할 배열이 필요
# 건물간의 관계 그래프 필요

# 위상정렬을 해나아가면서 최소값을 갱신한다.
from collections import deque
N = int(input())

buildtime = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
minresult = [0 for _ in range(N+1)]

in_degree = [0 for _ in range(N+1)]

for i in range(N):
    arr = list(map(int, input().split()))
    buildtime[i+1] = arr[0]
        
    for temp in range(1, len(arr)-1):
        graph[arr[temp]].append(i+1)
        in_degree[i+1] += 1

queue = deque()
for i in range(N):
    if in_degree[i+1] == 0:
        minresult[i+1] = buildtime[i+1]
        queue.append(i+1)
        
while queue:
    num = queue.popleft()
    
    for newnum in graph[num]:
        in_degree[newnum] -= 1
        minresult[newnum] = max(minresult[newnum], minresult[num] + buildtime[newnum])
        if in_degree[newnum] == 0:
            queue.append(newnum)
    
for result in minresult[1:]:
    print(result)
