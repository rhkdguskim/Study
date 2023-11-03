# https://www.acmicpc.net/problem/12869
import sys
input = sys.stdin.readline

N = int(input())
temp = list(map(int, input().split()))
scv = [0 for _ in range(3)]
for i in range(N):
    scv[i] = temp[i]
    
