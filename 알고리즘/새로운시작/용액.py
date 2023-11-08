# https://www.acmicpc.net/problem/246
import sys
input = sys.stdin.readline
INF = int(1e10) * 2 + 1 

N = input()
nums = list(map(int, input().split()))

p1 = 0
p2 = len(nums) - 1
ans = INF
ans_p1 = 0
ans_p2 = 0
while p1 < p2:
    cost = nums[p1] + nums[p2]
    if ans > abs(cost + 0):
        ans = abs(cost + 0)
        ans_p1, ans_p2 = nums[p1], nums[p2]
    if cost > 0:
        p2 -= 1
    else:
        p1 += 1

if ans_p1 > ans_p2:
    print(ans_p2 , ans_p1)
else:
    print(ans_p1 , ans_p2)
    