#https://www.acmicpc.net/problem/1976

def union(a, b):
    v1 = find(a)
    v2 = find(b)
    if v1 == v2: # 부모가 같을 경우 무시한다.
        return
    
    if v1 > v2:
        parent[v1] = v2
    else:
        parent[v2] = v1
        
def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
        
    return parent[a]

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

graph = []
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    
    
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i+1, j+1) # 그래프값이 1일경우 union 한다.
            
travel_list = list(map(int ,input().split()))

def travel():
    for i in range(1, len(travel_list)):
        if find(travel_list[i -1]) != find(travel_list[i]):
            print("NO")
            return
    
    print("YES")
    return

travel()