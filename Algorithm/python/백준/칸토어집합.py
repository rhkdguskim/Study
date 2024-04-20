# https://www.acmicpc.net/problem/4779
import sys
input = sys.stdin.readline

def dfs(i):
    if i == 0:
        return '-'
    
    result = dfs(i-1) + ' ' * pow(3, i-1) + dfs(i-1)
    return result

while True:
    try:
        n = int(input())
        print(dfs(n))
    except:
        break