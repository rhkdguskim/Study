import sys
input = sys.stdin.readline

N = int(input()) # 객차수(객차의 길이)
passenger = [0] + list(map(int, input().split())) # 객차에대한 손님정보
train_cnt = int(input()) # 최대 끌수 있는 객차 수

s = [0 for _ in range(N+1)]

s[0] = passenger[0]

for i in range(1, N+1): # 누적합을 계산한다.
    s[i] = s[i-1] + passenger[i]
    
def prefix_sum(start , end): # ex) a~b 까지의 손님수
    return s[end] - s[start] + passenger[start]

dp = [[0 for _ in range(N+1)] for _ in range(4)]

for i in range(1, 4):
    for j in range(i*train_cnt, N+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-train_cnt] + prefix_sum(j-train_cnt+1, j))

print(dp[3][N])