# https://www.acmicpc.net/problem/2629
import sys
input = sys.stdin.readline

weight_cnt = int(input())

weight = list(map(int, input().split()))

marble_cnt = int(input())

marble = list(map(int, input().split()))

dp = [False for _ in range(40001)]
for w in weight:
    to_update = set()
    for i in range(1, 40001):
        if dp[i] == True:
            to_update.add(abs(i-w))
            to_update.add(i+w)
            
        if w == i:
            to_update.add(i)
    
    for update in to_update:
        dp[update] = True

for i in range(marble_cnt):
    if dp[marble[i]]:
        print("Y", end = ' ')
    else:
        print("N", end =' ')

print("")