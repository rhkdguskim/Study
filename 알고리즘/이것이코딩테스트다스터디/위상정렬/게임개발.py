# https://www.acmicpc.net/problem/1516
# 최소값을 초기화하는 배열이 필요
# 건축시간을 갖고있는 배열이 필요

# 위상정렬을 할 배열이 필요
# 건물간의 관계 그래프 필요

# 위상정렬을 해나아가면서 최소값을 갱신한다.
from collections import deque
N = int(input())

buildtime = [0 for _ in range(N)]
graph = [[] for _ in range(N)]
minresult = [100000 * 501 for _ in range(N)]
table = [0 for _ in range(N)]

for i in range(N):
    arr = list(map(int, input().split()))
    buildtime[i] = arr[0]
    for temp in range(1, len(arr)):
        if arr[temp] != -1:
            table[arr[temp]-1] += 1
            graph[arr[temp]-1].append(i)

queue = deque()

for i in range(N):
    if table[i] == 0:
        queue.append((i+1, buildtime[i]))
        
while queue:
    num, cost = queue.popleft();
    minresult[num-1] = min(minresult[num-1], cost)
    print(num)
    for newnum in graph[num-1]:
        table[newnum-1] -= 1
        if table[newnum-1] == 0:
            queue.append((newnum-1, cost + buildtime[newnum-1]))
    
for result in minresult:
    print(result)
