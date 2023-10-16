# https://www.acmicpc.net/problem/2941
import sys
input = sys.stdin.readline

char = str(input())
N = len(char)
ans = 0
def dfs(cnt, depth):
    global ans
    if depth >= N-1:
        ans = cnt
        return

    if N > depth+1:
        if char[depth] == 'c':
            if char[depth+1] == '=' or char[depth+1] == '-':
                depth += 2
            else:
                depth += 1
        elif char[depth] == 'd':
            if char[depth+1] == '-':
                depth += 2
            elif char[depth+1] == 'z':
                depth += 3
            else:
                depth += 1
        elif char[depth] == 'l' or char[depth] == 'n':
            if char[depth+1] == 'j':
                depth += 2
            else:
                depth += 1
        elif char[depth] == 's' or char[depth] == 'z':
            if char[depth+1] == '=':
                depth += 2
            else:
                depth += 1
        else:
            depth += 1

        dfs(cnt+1, depth)
    else:
        dfs(cnt+1, depth+1)

dfs(0, 0)
print(ans)