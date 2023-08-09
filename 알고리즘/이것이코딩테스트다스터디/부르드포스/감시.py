# https://www.acmicpc.net/problem/15683
# CCTV를 하나씩 돌려보면서 최대 개수를 구한다.
# CCTV는 최대 8개 이므로, 4^8의 경우의 수가 나온다. (65536 가지)
# 탐색방법은 깊이우선탐색으로 한방향으로 가는 로직이기때문, 벽을 만나면 탐색종료
# 최소값 초기화조건은 모든 cctv로 구간을 모두 다 탐색했을때
# 2번과 5번은 중복되는 조건이 있다.
cctv = [1,2,3,4,5]
move = []
move.append([]) # dummy 0번 cctv
move.append(([(0,1)], [(0,-1)], [(1,0)], [(-1,0)])) # dummy 1번 cctv
move.append(([(0,1), (0,-1)], [(1,0), (-1,0)])) # dummy 2번 cctv
move.append(([(0,1), (0,-1)], [(0,-1), (1,0)] , [(0,-1), (1,0)] , [(0,-1), (1,0)])) # dummy 3번 cctv
move.append(([(0,-1), (-1,0), (0,1)], [(-1,0), (0,1), (1,0)], [(0,1), (1,0), (0,-1)], [(1,0), (0,-1), (-1,0)])) # dummy 4번 cctv
move.append(([(1,0), (-1,0), (0,1), (0,-1)])) # dummy 5번 cctv
N, M = map(int, input().split()) # N은 세로크기, M은 가로크기
graph = []
cctvlist = []
for i in range(N):
    table = list(map(str, input().split()))
    for j in range(M):
        if table[j] in cctv:
            cctvlist.append((i,j))
    graph.append(table)
    
print(move)

def dfs(i,j, movetype):
    if N > i >= 0 and M > j >=0:
        dy = movetype[0]
        dx = movetype[1]
        ny = i + dy
        nx = j + dx
        if N > ny >= 0 and M > nx >=0 and graph[ny][nx] == '0': # 빈칸이면 들어가본다.
            graph[ny][nx] = '#'
            dfs(ny,nx)
            graph[ny][nx] = '0'
        
    else:
        return

minvalue = 64
def cctvArea(depth):
    global minvalue
    if len(cctvlist) == depth:
        minvalue = min(minvalue, graph.count('0'))
        return
    
    for cctv in cctvlist:    
        for moves in move[graph[cctv[0]][cctv[1]]]:
            for trymove in moves:
                dfs(cctv[0], cctv[1], trymove)