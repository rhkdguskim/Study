# https://www.acmicpc.net/problem/15681
import sys
input = sys.stdin.readline

N, R, Q = map(int, input().split())
edge = [[] for _ in range(N+1)]
cnt_node = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]

def init(n):
    #print("node", n)
    visited[n] = True
    
    if len(edge[n]) == 1:
        cnt_node[n] = 1
        return 1
    
    cnt = 0
    for newnode in edge[n]:
        if not visited[newnode]:
            cnt += init(newnode)
    
    cnt_node[n] = cnt + 1
    #print("nodecnt", n, cnt_node[n])
    return cnt_node[n]

for _ in range(N-1):
    U, V = map(int, input().split())
    edge[U].append(V)
    edge[V].append(U)

init(R)

for _ in range(Q):
    n = int(input())
    print(cnt_node[n])