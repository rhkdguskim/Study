# https://www.acmicpc.net/problem/20061
import sys
from collections import deque
from bisect import bisect_left



input = sys.stdin.readline
D, N = map(int, input().split()) # 오븐의 깊이, 피자의 개수

oven = list(map(int, input().split())) # 오븐의 길이를 맞추기 위해 Dummy 값 넣기
pizza = deque(map(int, input().split()))

for i in range(1, len(oven)):
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]

print(oven)
start = 0
end = D-1

while start <= end:
    mid = (start + end) // 2
    
    if 5 < oven[mid]:
        start = mid + 1
    else:
        end = mid
        
        
    print(mid)

