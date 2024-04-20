# https://www.acmicpc.net/problem/21610
# 각 끝은 연결되어있다.
# (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다.
# 구름이 이동한다. 구름을 이동한뒤에 그 위치에 바구니에 저장된 물이 1이 증가한다.
# 구름이 사라진다.
# 증가한 곳에서 물복사 버그를 시전한다. 대각선 방향으로 1인 칸에 물이 있는 바구니 수 만큼 (r, c)에 있는 바구느이 물이 양이 증간한다.
# 바구니에 저장된 물의 양이 2이상인곳에 모든 구름이 생긴다. 생기는 구름은 이전에 그룸이 아니었던 그룸이어야한다.

# 그룸을 이동시키는 로직
# 그룸을 통하여 바구니에 저장된 물이 양이 증가
# 물복사 버그 마법 시전
# 바구니에 저장된 물의 양이 2이상인 모든칸에 구름이 생기고 물이양이 2 줄어든다.

import sys
input = sys.stdin.readline

N, M = map(int ,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


def change_range(y, x):
    if N > y >= 0 and N > x >=0:
        return y, x
    else:
        if y == N:
            y = 0
        
        if y == -1:
            y = N-1
            
        if x == N:
            x = 0
        
        if x == -1:
            x = N-1
            
        return y, x

def move_cloud(cloud, d, s): #구름, 방향, 거리
    moves = [(0, 0),(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    moved_cloud = set()
    for y, x in cloud:
        temp_y, temp_x = y, x
        for _ in range(s):
            dy, dx = moves[d][0], moves[d][1]
            ny, nx = dy + temp_y, dx + temp_x
            temp_y, temp_x = change_range(ny, nx)
        
        moved_cloud.add((temp_y, temp_x))
    
    return moved_cloud

def rain_and_copy_bug(cloud):
    moves = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    for y, x in cloud:
        graph[y][x] += 1
        
    for y, x in cloud:
        for dy, dx in moves:
            ny, nx = dy + y, dx + x
            if N > ny >=0 and N > nx >=0 and graph[ny][nx]:
                graph[y][x] += 1
    

def make_clude(cloud):
    new_cloud = set()
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2:
                if (i, j) not in cloud:
                    graph[i][j] -= 2
                    new_cloud.add((i, j))
                
    return new_cloud

def sum_bucket():
    ans = 0
    for i in range(N):
        for j in range(N):
           ans += graph[i][j] 
    
    return ans
    
cloud = set([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])
for _ in range(M):
    d, s = map(int, input().split())
    cloud = move_cloud(cloud, d, s)
    rain_and_copy_bug(cloud)
    cloud = make_clude(cloud)
    
print(sum_bucket())