# https://www.acmicpc.net/problem/1987
import sys

input = sys.stdin.readline

R, C = map(int, input().split())

table = [list(str(input())) for _ in range(R)]

def dfs(y, x, visited, cnt):
    if visited & (1 << ord(table[y][x])):
        return cnt
    
    if visited in v[y][x]:
        return 0
    
    visited |= (1 << ord(table[y][x]))
    
    max_distance = 0
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny, nx = dy + y, dx + x
        if R > ny >=0 and C > nx >=0:
            max_distance = max(dfs(ny, nx, visited, cnt + 1), max_distance)
    
    v[y][x].add(visited)
    visited &= ~(1 << ord(table[y][x]))
    
    return max_distance

print(dfs(0, 0, 0, 0))