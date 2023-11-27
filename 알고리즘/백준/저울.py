# https://www.acmicpc.net/problem/2437
import sys
input = sys.stdin.readline

N = int(input())

chu = list(map(int, input().split()))
chu.sort()

max_chu = 0
for c in chu:
    if c > max_chu:
        if abs(c - max_chu) > 1:
            break
        else:
            max_chu += c
    else:
        max_chu += c
        
print(max_chu + 1)