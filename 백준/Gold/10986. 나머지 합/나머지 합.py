import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

remainder_count = defaultdict(int)
remainder_count[0] = 1 

prefix_sum = 0
ans = 0

for num in arr:
    prefix_sum += num
    remainder = prefix_sum % M

    if remainder < 0:
        remainder += M

    ans += remainder_count[remainder]

    remainder_count[remainder] += 1

print(ans)