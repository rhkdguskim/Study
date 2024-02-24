# https://www.acmicpc.net/problem/1351

# 시간복잡도는 LogN 으로 풀어하는데 P와 Q가 2보다 큼으로, 최소 수가 반씩 줄어들어 logN이 나온다.
# 깊이우선탐색 + 다이나믹프로그램으로 문제를 해결하면된다.
import sys
from collections import defaultdict

input = sys.stdin.readline
N, P, Q = map(int, input().split())
dp = defaultdict(int)

def A(num):
    if num == 0:
        dp.setdefault(num, 1)
        return 1
    
    if num in dp:
        return dp[num]
    
    left = num // P
    right = num // Q
    
    dp.setdefault(num, A(left) + A(right))
    
    return dp[num]

print(A(N))