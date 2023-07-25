from collections import deque
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int ,input().split())))

minvalue = int(10e9)

def dfs(start, nodelist, sum):
    global minvalue
    if sum > minvalue:
        return int(10e9)
    
    if len(nodelist) == N:
        #print(nodelist, sum)
        if graph[start][nodelist[0]]:
            minvalue = min(minvalue, sum + graph[start][nodelist[0]]) # 마지막은 자기자신으로 방문한다. 마지막도착지점에서 자기자신으로 갈 수 없을 경우
            return minvalue
        else:
            return int(10e9)
    
    for x in range(N):
        if x not in nodelist:
            if graph[start][x] == 0: # 갈수없는 경우 순회중단
                return int(10e9)
            sum += graph[start][x]
            nodelist.append(x)
            dfs(x,nodelist, sum)
            nodelist.pop()
            
    return minvalue

minvalue = int(10e9)
nodelist = deque()
for i in range(N):
    nodelist.append(i)
    minvalue = min(dfs(i,nodelist, 0), minvalue)
    end = nodelist.pop()
        
        
print(minvalue)