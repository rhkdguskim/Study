import sys
from itertools import combinations_with_replacement as cwr

input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])[::-1]
arr_sum = {x+y for x, y in cwr(arr, 2)}

for i in arr:
    for j in arr:
        if i >= j and (i-j) in arr_sum:
            print(i)
            exit()