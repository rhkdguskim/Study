import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
temp = set(map(int, input().split()))

ranked = []
for i in temp:
    idx = bisect_left(ranked, -i)
    ranked.insert(idx, -i)

M = int(input())
player = list(map(int, input().split()))
result = []
for p in player:
    idx = bisect_left(ranked, -p)
    result.append(idx+1)
    if idx < len(ranked) and ranked[idx] == -p:
        continue

    ranked.insert(idx, -p)

for num in result:
    print(num)