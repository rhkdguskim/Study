# https://www.acmicpc.net/problem/16235
# 봄 (나무가 양분을 먹는다.)
# 1x1 자리에서 자신의 나이만큼 양분을 먹는다, 작은 나무부터 양분을 먹는다.
# 양분을 먹을 수 없는 나무는 즉시 죽는다.
# 여름 ( 죽은 나무가 양분으로 바뀜 )
# 죽은 나무가 양분으로 변한다. 죽은나무마다 나이를 2로 나눈값이 나무가 있던 칸에 양분으로 추가된다.

# 가을 ( 나무가 번식한다. ) 
# 번식하는 나무는 나이가 5의 배수이며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
# 겨울
# 양분을 추가한다. 양분의 양은 입력으로 주어진다.

# N 땅크기, M 나무 개수, K년
# k년후 나무의 개수를 구하시오.
import sys
from collections import deque

nears = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

input = sys.stdin.readline

N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
tree = []
for _ in range(M):
    x, y, z = map(int, input().split())
    tree.append((x, y, z))


# 양분은 5
land = [[[5, deque()] for _ in range(N+1)] for _ in range(N+1)]

tree.sort(key=lambda x:x[2])

for i, j, age in tree:
    land[i][j][1].append(age)
    
    
def spring_summer():
    dead_tree = deque()
    for i in range(1, N+1):
        for j in range(1, N+1):
            trees = land[i][j][1]
            live_tree = deque()
            for age in trees:
                if land[i][j][0] >= age:
                    land[i][j][0] -= age
                    live_tree.append(age+1)
                else:
                    dead_tree.append((i, j, age))
            land[i][j][1] = live_tree
            
    for i, j, age in dead_tree:
        land[i][j][0] += age//2

def fall_winter():
    for i in range(1, N+1):
        for j in range(1, N+1):
            trees = land[i][j][1]
            land[i][j][0] += A[i-1][j-1]
            for age in trees:
                if age % 5 == 0:
                    for dy, dx in nears:
                        ny, nx = dy + i, dx + j
                        if N >= ny >0 and N >= nx > 0:
                            land[ny][nx][1].appendleft(1)
                            
for _ in range(K):
    spring_summer()
    fall_winter()
    
ans = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        trees = land[i][j][1]
        ans += len(trees)
        
print(ans)