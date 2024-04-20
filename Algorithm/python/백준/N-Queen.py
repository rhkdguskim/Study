# https://www.acmicpc.net/problem/9663
# 해당위치에 놓을 수 있다면, 다음 행을 탐색한다.
# 해당위치에 놓을 수 없다면, 다음 열을 탐색한다.
# 놓을 수 없는경우 조건을 구한다.
# 행이 같은경우, 열이 같은경우, 대각선으로 겹치는경우
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

N = int(input())

def check(i, j, queens:list):
    for q_y, q_x in queens:
        # 열이 같은경우
        if q_y == i:
            return False

        # 행이 같은경우
        if q_x == j:
            return False
        
        # 대각선에 놓인경우
        if abs(q_y - i) == abs(q_x - j):
            return False

    return True

def dfs(row, col, queens:list):
    if len(queens) == N: # 모두 다 놓았을 경우.
        return 1
    
    total = 0
    for row in range(N):
        if check(row, col, queens):
            queens.append((row, col))
            total += dfs(row, col+1, queens)
            queens.pop()
            
    return total

print(dfs(0,0, []))