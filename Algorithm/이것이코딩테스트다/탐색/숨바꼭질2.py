# https://www.acmicpc.net/problem/13549
from collections import deque
INF = int(10e9)
N, K = map(int, input().split())

dp = [INF for _ in range(100000+1)] # dp 테이블을 무한대 값으로 초기화한다.

moves = ['front','back','double'] # 앞, 뒤, x2

queue = deque()
def findbrother(start, end):
    queue.appendleft(start)
    dp[start] = 0
    while queue:
        now = queue.pop()
        if now == end :
            break
        for move in moves:
            if move == "front":
                if end+2 > now+1 and dp[now+1] > dp[now] + 1: # 주의 !! end+2 만큼 탐색해야 최소값을 얻을 수 있다. 999는 1000에서의 한칸뒤로간 값
                    dp[now+1] = dp[now] + 1
                    queue.appendleft(now+1)
            elif move == "back":
                if now-1 >= 0  and dp[now-1] > dp[now] + 1:
                    dp[now-1] = dp[now] + 1
                    queue.appendleft(now-1)
            elif move == "double":
                if end+2 > now*2 and dp[now*2] > dp[now]: # 주의 !! end+2 만큼 탐색해야 최소값을 얻을 수 있다. 999는 1000에서의 한칸뒤로간 값
                    dp[now*2] = dp[now]
                    queue.appendleft(now*2)

findbrother(N,K)
print(dp[K])