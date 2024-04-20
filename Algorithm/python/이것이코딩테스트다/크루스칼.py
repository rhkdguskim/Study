import sys
input = sys.stdin.readline

N = int(input()) # 간선의 개수

def getParent(parent, a):
    if parent[a] != a: # 루트 노드가 아니라면
        parent[a] = getParent(parent, parent[a])
        
    return parent[a]

def union(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

queue = []
parent = [0 for _ in range(N+1)]

for i in range(1,N+1): # 루트노드르 자기자신으로 초기화
    parent[i] = i 

for _ in range(N):
    a, b, cost = map(int,input().split())
    queue.append((cost, a, b))
    
queue.sort() # 가장 짧은 간선부터 뽑아야 하기 때문에 cost 로 정렬

result = 0
for edge in queue:
    cost, a,b = edge
    if getParent(parent, a) != getParent(parent,b): # 둘이 사이클이 아니라면
        union(parent, a, b) # 둘이 합친다 = 간선을 추가
        result += cost # 이동 비용을 누적한다.
    
print(result) # 비용 출력
    