# https://www.acmicpc.net/problem/2212
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

sensor = list(map(int, input().split()))
sensor.sort()

dist = []
for i in range(1, N):
    dist.append((sensor[i] - sensor[i-1]))

dist.sort()
for _ in range(K-1):
    if dist:
        dist.pop()

if K >= N:
    print(0)
else:
    print(sum(dist))