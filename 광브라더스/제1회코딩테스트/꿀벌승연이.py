# 깊이 우선 탐색이나 이미 탐색 중복한 부분은 탐색하지않아야한다.
# 중복탐색조건(다이나믹 프로그래밍)

# 정수 삼각형 문제를 생각 할 수 있다.
# 마지막 도착지점에서 시작하여 해당 노드로 올수 있는 경우를 구한다.
import sys
sys.setrecursionlimit(10**9)
N, M = map(int, input().split()) # N은 세로, M은 가로
RESULT = int(1e9 + 7)
table = [[1 for _ in range(M)] for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
move = [(1,0), (-1,1), (0,1)] # 홀수일때
move2 = [(1,0), (0,1), (1,1)] # 홀수일때
K = int(input()) # 구멍칸의 개수

for _ in range(K):
    a, b = map(int, input().split())
    table[a-1][b-1] = 0

def dfs(i,j):
    if i == N-1 and j == M-1:
        visited[i][j] = 1
        return 1
     
    if visited[i][j] != -1:
        return visited[i][j]
    
    visited[i][j] = 0

    for k in range(3):
        newy, newx  = 0 ,0
        if j % 2 == 1: # 홀수일때
            newy , newx = move2[k]
        else: # 짝수일때
            newy , newx = move[k]
        dy = i + newy
        dx = j + newx
        if N > dy >=0 and M > dx >=0 and table[dy][dx] == 1:
            visited[i][j] += (dfs(dy,dx) % RESULT)

    return visited[i][j]


dfs(0,0)
print(visited[0][0] % RESULT)