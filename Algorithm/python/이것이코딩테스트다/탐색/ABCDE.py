# https://www.acmicpc.net/problem/13023
import sys
sys.setrecursionlimit(100000)
N , M = map(int ,input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

def dfs(start):
    global isFriend
    if len(queue) == 5:
        isFriend = True
        return
    
    for friend in graph[start]:
        if friend not in queue:
            queue.add(friend)
            dfs(friend)
            queue.remove(friend)
            
queue = set()
isFriend = False
for i in range(N):
    queue.add(i)
    dfs(i)
    queue.remove(i)
    if isFriend:
        break

if isFriend:
    print(1)
else:
    print(0)