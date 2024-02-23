# https://www.acmicpc.net/problem/1525
import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

puzzle = []
for _ in range(3):
    puzzle.append(list(map(int, input().split())))
    
def serialize(puzzle):
    temp = ''
    for i in range(3):
        temp += ''.join(map(str, puzzle[i]))
    
    return temp

def deserialize(string):
    temp = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[i][j] = string[i*3+j]
            
    return temp

def find_zero(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == '0':
                return i, j

def is_made(puzzle):
    return puzzle == '123456780'
    


def solove(p):
    is_not_found = True
    visited = set()
    start = serialize(p)
    visited.add(start)
    queue = deque([(start, 0)])
    while queue:
        puzzle, cnt = queue.popleft()
        
        if is_made(puzzle):
            is_not_found = False
            print(cnt)
            break
        
        
        temp = deserialize(puzzle)
        y, x = find_zero(temp)
        
        for dy, dx in [(0,1), (0,-1), (1,0), (-1,0)]:
            ny, nx = y + dy, x + dx
            if 3 > ny >=0 and 3 > nx >=0:
                table = deepcopy(temp)
                table[y][x], table[ny][nx] = table[ny][nx], table[y][x]
                check = serialize(table)
                if check not in visited:
                    visited.add(check)
                    queue.append((check, cnt + 1))
                    
    if is_not_found:
        print(-1)

solove(puzzle)

