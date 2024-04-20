# https://www.acmicpc.net/problem/12904

import sys
input = sys.stdin.readline

S = list(str(input().strip()))
T = list(str(input().strip()))


def dfs(target):
    if len(target) == 0:
        return False
    
    if ''.join(S) == ''.join(target):
        return True
    
    flag1 = False
    if target[-1] == 'A':
        flag1 = dfs(target[:-1])
        
    flag2 = False
    reversed_char = list(reversed(target))
    if reversed_char[0] == 'B':
        flag2 = dfs(reversed_char[1:])
    
    return flag1 or flag2

ans = dfs(T)
if ans:
    print(1)
else:
    print(0)