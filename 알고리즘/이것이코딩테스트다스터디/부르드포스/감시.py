# https://www.acmicpc.net/problem/15683
# CCTV를 하나씩 돌려보면서 최소사각지대 감시구역 테이블을 구한다.
# 8개의 모든 감시테이블을 구하면 합쳐서 다시 최소사각지대 감시 구역을 계산한다.
import copy
import pprint
cctv = ['1','2','3','4','5']
N, M = map(int, input().split()) # N은 세로크기, M은 가로크기
graph = []
cctvlist = []
for i in range(N):
    table = list(map(str, input().split()))
    for j in range(M):
        if table[j] in cctv:
            cctvlist.append((i,j))
    graph.append(table)

def sumBilndArea(tables): # 8개 이하의 CCTV의 최소 테이블을 합쳐서 값을 Return 한다.
    newtable = [['0' for _ in range(M)] for _ in range(N)]
    counter = 0
    for table in tables:
        for i in range(N):
            for j in range(M):
                if table[i][j] != '0' and newtable[i][j] == '0':
                    newtable[i][j] = '#'
                    counter += 1
    pprint.pprint(newtable)
    return M*N - counter

def getBlindSpot(table): # 사각지대를 return 한다.
    counter = 0
    for i in range(N):
        for j in range(M):
            if table[i][j] == '0':
                counter+=1           
    return counter

def dfs(i,j, move, table):
    ny = i + move[0]
    nx = j + move[1]
    if N > ny >=0 and M > nx >=0 and table[ny][nx] != '6':
        table[ny][nx] = '#'
        dfs(ny,nx, move, table)
    

def cctvBlindArea(curcctv): # cctv 감시구역 테이블을 계산한뒤 최소값의 테이블을 리턴한다.
    for cctv in cctvlist:
        if cctv not in curcctv:
            curcctv.append(cctv)
            y = cctv[0]
            x = cctv[1]
            for mov in move[graph[y][x]]:
                for trymove in mov:
                    dfs(i,j, move ,table)

tables = []
move = [[],
        [[(0,1)],[(0,-1)], [(1,0)], [(-1,0)]],  #1번
        [[(1,0), (-1,0)], [(0,1), (0,-1)]], # 2번
        [[(-1,0), (0,1)], [(0,1), (1,0)], [(1,0), (0,-1)], [(-1,0), (0,-1)]], # 3번
        [[(0,-1), (0,1), (-1,0)], [(1,0), (0,1), (-1,0)], [(1,0), (0,1), (0,-1)], [(1,0), (-1,0), (0,-1)]],  # 4번
        [[(0,1), (1,0), (-1,0), (0,-1)]]] # 5번
for i,j in cctvlist:
    moves = move[int(graph[i][j])] # CCTV 타입에따라 돌려보는 각도를 구한다.
    tables.append(cctvBlindArea(i,j,moves, graph))


print(sumBilndArea(tables))