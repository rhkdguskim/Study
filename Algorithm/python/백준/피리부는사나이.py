# https://www.acmicpc.net/problem/16724
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(str, input().strip())) for _ in range(N)]
direction = ['U', 'D', 'L', 'R']
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
parent = [i for i in range(N*M)]

def find(v1):
    if parent[v1] != v1:
        parent[v1] = find(parent[v1])
        return parent[v1]

    return parent[v1]

def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    
    if p1 > p2:
        parent[p1] = p2
    else:
        parent[p2] = p1
        
def start(i, j):
    index = direction.index(table[i][j])
    dy, dx = move[index]
    ny, nx = dy + i, dx + j
    v1 = i*M + j%M
    v2 = ny*M + nx%M
    p1 = find(v1)
    p2 = find(v2)
    if p1 == p2:
        return
    else:
        union(p1, p2)
        start(ny, nx)
        return


for i in range(N):
    for j in range(M):
        start(i, j)
        
print(len(set(parent)))