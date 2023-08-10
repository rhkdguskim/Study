# https://www.acmicpc.net/problem/15683
# CCTV를 하나씩 돌려보면서 최소사각지대 감시구역 테이블을 구한다.
# 8개의 모든 감시테이블을 구하면 합쳐서 다시 최소사각지대 감시 구역을 계산한다.
import copy
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
    
    for table in tables:
        for i in range(N):
            for j in range(M):
                if table[i][j] != '0':
                    newtable[i][j] = '#'
                    
    return newtable.count('0')

def getBlindSpot(table): # 사각지대를 return 한다.
    counter = 0
    for i in range(N):
        for j in range(M):
            if table[i][j] == '0':
                counter+=1
                
    return counter

def cctvBlindArea(i,j, moves, table): # cctv 감시구역 테이블을 계산한뒤 최소값의 테이블을 리턴한다.
    minvalue = N*M
    resulttable = []
    for move in moves:
        for mov in move:
            newtable = copy.deepcopy(table)
            ny = i + mov[0]
            nx = j + mov[1]
            if N > ny >=0 and M > nx >=0 and newtable[ny][nx] == '0':
                newtable[ny][nx] == '#'
                
        cost = getBlindSpot(newtable)
        if cost > minvalue:
            minvalue = cost
            resulttable = copy.deepcopy(newtable)
                    
    return resulttable

tables = []
move = [[],[[(0,1)],[(0,-1)], [(1,0)], [(-1,0)]], [[(1,0), (-1,0)], [[(0,1), (0,1)]]], [[(-1,0), (0,1)], [(0,1), (1,0)], [(1,0), (0,-1)], [(-1,0), (0,-1)]], [[(0,-1), (0,1), (-1,0)], [(1,0), (0,1), (-1,0)], [(1,0), (0,1), (0,-1)], [(1,0), (-1,0), (0,-1)]], [[(0,1), (1,0), (-1,0), (0,-1)]]]
for i,j in cctvlist:
    moves = move[int(graph[i][j])] # CCTV 타입에따라 돌려보는 각도를 구한다.
    print(moves)
    tables.append(cctvBlindArea(i,j,moves, graph))


print(sumBilndArea(tables))