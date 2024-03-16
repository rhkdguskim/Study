# https://www.acmicpc.net/problem/17822
import sys
from collections import deque
input = sys.stdin.readline
DIR = 0 # 시계방향
IN_DIR = 1 # 반시계방향

N, M, T = map(int, input().split())

graph = [deque(list(map(int, input().split()))) for _ in range(N)]

filter = lambda y, x : (y, (x+M) % M)
is_range = lambda y, x : (N > y >= 0 and M > x >=0)

def rotate(d, dir):
    if dir == DIR:
        graph[d].appendleft(graph[d].pop())
    else:
        graph[d].append(graph[d].popleft())

def find_near_num_and_avg():
    nums = set()
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    total = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != None:
                total += graph[i][j]
                cnt += 1
                for dy, dx in moves:
                    ny, nx = dy + i, dx + j
                    ny, nx = filter(ny, nx)
                    if graph[i][j] and is_range(ny, nx) and graph[ny][nx]:
                        if graph[i][j] == graph[ny][nx]:
                            nums.add((i, j))
                            nums.add((ny, nx))
    if cnt != 0:
        avg = total/cnt
    else:
        avg = 0
    return nums, avg

def no_number_command(avg):
    for i in range(N):
        for j in range(M):
            if graph[i][j] != None:
                if graph[i][j] > avg:
                    graph[i][j] -= 1
                elif graph[i][j] < avg:
                    graph[i][j] += 1

def sum_graph():
    total = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != None:
                total += graph[i][j]
    
    return total

for _ in range(T):
    x, d, k = map(int, input().split())
    for i in range(x, N+1, x):
        for _ in range(k):
            rotate(i-1, d)
    
    nums, avg = find_near_num_and_avg()
    if len(nums) == 0:
        no_number_command(avg)
    else:
        for i, j in nums:
            graph[i][j] = None

print(sum_graph())
    