# https://www.acmicpc.net/problem/1068
# 1. 해당 노드가 leaf노드인지 판별하는 함수 작성
# 2. 해당 노드가 leaf노드인지 판별하는 방법 - 자식이 0 이면 해당노드는 leaf 노드이다. -> 자식노드의 개수를 return 하는 함수를 만든다.
N = int(input())
nodeInput = list(map(int ,input().split()))
deletedNode = int(input())
graph = [[] for _ in range(N)]
rootnode = 0
for i in range(len(nodeInput)):
    if nodeInput[i] >= 0:
        graph[nodeInput[i]].append(i)
    else:
        rootnode = i
    
cnt = 0

def leafNode(node):
    global cnt
    childnode_cnt = len(graph[node]) # 자식노드 개수 init
    for childnode in graph[node]:
        if childnode != deletedNode: # 지워진 노드가 아니라면
            if leafNode(childnode) == 0:
                cnt += 1
        else: # 지워진 노드라면
            childnode_cnt -= 1 # 해당노드를 자식에서 지운다.
    
    return childnode_cnt

if leafNode(rootnode) == 0:
    cnt += 1

if rootnode == deletedNode: # 루트노드가 지워진 노드 예외 처리
    print(0)
else:
    print(cnt)