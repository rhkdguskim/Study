# https://www.acmicpc.net/problem/16235
import sys
from collections import deque
from copy import deepcopy
from pprint import pprint

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
land = [[5 for _ in range(N+1)] for _ in range(N+1)]
ar = [[0 for _ in range(N+1)] for _ in range(N+1)]
tree = [[deque() for _ in range(N+1)] for _ in range(N+1)]
move = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

for i in range(1, N+1):
    ar[i] = [0] + list(map(int, input().split()))

for _ in range(M):
    y, x, z = map(int, input().split())
    tree[y][x].append(z)

def spring_sumer(land, tree):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            newtree = deque()
            died = 0
            while tree[i][j]:
                size = tree[i][j].popleft()
                if land[i][j] >= size:
                    land[i][j] -= size
                    newtree.append(size+1)
                else:
                    died += size//2

            tree[i][j] = newtree
            land[i][j] += died
def fall_winter(tree, ar):
    temp_tree = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            land[i][j] += ar[i][j]
            for size in tree[i][j]:
                if (size % 5) == 0: # 5의 배수이면 나머지 값이 0이다.
                    for dy, dx in move:
                        ny = dy + i
                        nx = dx + j
                        if N >= ny >= 1 and N >= nx >= 1:
                            temp_tree.append((ny, nx))

    for y, x in temp_tree:
        tree[y][x].appendleft(1)

def getalivetree(tree):
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            cnt += len(tree[i][j])

    return cnt

while K > 0:
    spring_sumer(land, tree)
    fall_winter(tree, ar)
    K -= 1

print(getalivetree(tree))