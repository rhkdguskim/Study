# https://www.acmicpc.net/problem/12015
# https://www.acmicpc.net/problem/12738

import sys
from bisect import bisect_left

input = sys.stdin.readline


N = int(input())
sub_sequence = list(map(int, input().split()))

lss = [sub_sequence[0]]

for i in range(1, len(sub_sequence)):
    if sub_sequence[i] > lss[-1]:
        lss.append(sub_sequence[i])
    else:
        idx = bisect_left(lss, sub_sequence[i])
        lss[idx] = sub_sequence[i]
    
print(len(lss))