# https://www.acmicpc.net/problem/1911
import sys
input = sys.stdin.readline

N, L = map(int, input().split())

water = []
for _ in range(N):
    water.append(tuple(map(int, input().split())))

water.sort()

pos = 0
cnt = 0
for start, end in water:
    if start > pos:
        pos = start
    
    while end > pos:
        pos += L
        cnt += 1

print(cnt)

from sys import stdin
input = stdin.readline
n, l = map(int, input().split())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
p.sort(key=lambda x: x[0])
last = p[0][0]
cnt = 0
for i in range(n):
    if last < p[i][0]:
        last = p[i][0]
    ccnt = (p[i][1] - last) // l
    if (p[i][1] - last) % l != 0:
        ccnt += 1
    # print(p[i][0], p[i][1], last, ccnt, cnt)
    last += ccnt * l
    cnt += ccnt
    
print(cnt)