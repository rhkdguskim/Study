# https://www.acmicpc.net/problem/18809
# 초록색과 빨간색 배양액을 적절하게 뿌려서 꽃을 피운다.
# 배양액을 넣을 곳은 정해져있다.
# 배양액은 매 초마다 이전에 배양액이 도달한 적이 없는 인접한 땅으로 퍼져간다.
# 하얀색 땅, 황토색 배양액을 뿌릴수 있는땅, 하늘색 호수
# 0은호수, 1은 배양액을 뿌릴 수 없는 땅, 2는 배양액을 뿌릴수 있는땅
import sys
input = sys.stdin.readline

from itertools import combinations
from collections import deque

def BFS():
    flower = 0
    while queue:
        y,x,ylast,xlast,time,color = queue.popleft()
            
        if visited[ylast][xlast] == 1:
            continue
        
        if visited[y][x]:
            if visited[y][x] == (time,-color):
                visited[y][x] = 1
                flower += 1
            continue

        visited[y][x] = (time,color)
        
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = y+dy, x+dx
            if N>ny>=0 and M>nx>=0 and garden[ny][nx]:
                queue.append((ny,nx,y,x,time+1,color))
            
    return flower
    

N,M,G,R = map(int,input().split())

garden = []
for i in range(N):
  garden.append([*map(int,input().split())])

spread = []
for i in range(N):
  for j in range(M):
    if garden[i][j] == 2:
        spread.append((i,j))

result = 0
for GRlist in combinations(spread, G+R):
    for Glist in combinations(GRlist,G):
        visited = [[0]*M for _ in range(N)]
        queue = deque()
        
        for y,x in Glist:
            visited[y][x] = 1
            queue.append((y,x,y,x,1,1)) # green
            
        for y,x in GRlist:
            if visited[y][x]:
                continue
            queue.append((y,x,y,x,1,-1)) # red
      
    visited = [[0]*M for _ in range(N)]
    result = max(result,BFS())

print(result)