# https://www.acmicpc.net/problem/2616
import sys
input = sys.stdin.readline

N = int(input()) # 객차수(객차의 길이)
passenger = list(map(int, input().split())) # 객차에대한 손님정보
train_cnt = int(input()) # 최대 끌수 있는 객차 수

s = [0 for _ in range(N)]

s[0] = passenger[0]

for i in range(1, N): # 누적합을 계산한다.
    s[i] = s[i-1] + passenger[i]
    
def prefix_sum(start , end): # ex) a~b 까지의 손님수
    return s[end] - s[start] + passenger[start]

ans = 0

dp = [[-1 for _ in range(3)] for _ in range(N)]

def dfs(idx, cnt):
    if cnt == 3: # 3개의 조합을 다 생성했다면
        return 0
    
    if dp[idx][cnt] != -1:
        return dp[idx][cnt]
    
    for i in range(idx, N):
        for n_train_cnt in range(train_cnt, 0, -1):
            start = i
            end = i + n_train_cnt - 1
            if N > end+1:
                cost = prefix_sum(start, end)
                dp[idx][cnt] = max(dp[idx][cnt], dfs(end+1, cnt+1) + cost)
                
    return dp[idx][cnt]
            

print(dfs(0, 0))