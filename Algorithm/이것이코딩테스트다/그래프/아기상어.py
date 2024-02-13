# https://www.acmicpc.net/problem/16236
from collections import deque
from bisect import bisect_left
INF = int(10e9)
N = int(input()) # 공간의 크기
moves = [[1,0], [-1,0], [0,1], [0,-1]]
space = []
sharkpos = [] #sharkpos[0]은 세로위치 sharkpos[1]은 가로위치
for i in range(N):
    arr = list(map(int, input().split()))
    space.append(arr)
    for j in range(len(arr)):
        if arr[j] == 9:
            sharkpos.append(i) # 세로값
            sharkpos.append(j) # 가로값

def getSmallFishList(i,j,level):
    que = deque()
    dp = [[INF for _ in range(N)] for _ in range(N)]
    que.append([i,j,0])
    fishlist = []
    while que:
        di,dj, distance = que.popleft()
        for dy, dx in moves:
            ny = di + dy
            nx = dj + dx
            cost = distance + 1
            if N > ny >= 0 and N > nx >=0 and level >= space[ny][nx] and dp[ny][nx] > cost:
                dp[ny][nx] = cost
                que.append([ny, nx, cost])
                if space[ny][nx] != 0 and level > space[ny][nx]:
                    fishlist.append([cost,ny,nx]) # 움직여야하는 거리값, ny, nx
                
    fishlist = deque(sorted(fishlist, key=lambda x: (x[0], x[1], x[2])))
    return fishlist

queue = deque()
space[sharkpos[0]][sharkpos[1]] = 0
queue.append([sharkpos[0], sharkpos[1], 2, 0]) # 세로위치, 가로위치, 레벨, 경험치
distance = 0
while queue:
    i,j,level,exp = queue.popleft()
    fishlist = getSmallFishList(i,j,level)
    if fishlist:
        dis, y, x = fishlist[0]
        distance += dis
        space[y][x] = 0 # 먹어버림
        exp += 1
        if exp == level:
            level +=1
            exp = 0
        
        queue.append([y, x, level, exp])
            
print(distance)