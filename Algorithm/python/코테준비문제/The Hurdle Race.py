# https://www.hackerrank.com/challenges/the-hurdle-race/problem?isFullScreen=true
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
height = list(map(int, input().split()))
height.sort(reverse=True)
if k >= height[0]:
    print(0)
else:
    print(height[0] - k)