import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
eat_value = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(K):
    a, b, c = map(int, input().split())
    eat_value[a][b] = max(eat_value[a][b], c)

dp = [[-1 for _ in range(M+1)] for _ in range(N+1)] # -1로 초기화
dp[1][1] = 0  # 시작 도시의 기내식 점수는 0

for m in range(1, M+1):
    for u in range(1, N+1):
        if dp[u][m] == -1:  # 해당 도시에 도착하지 않았으면 건너뛴다
            continue
        for v in range(u+1, N+1):
            if eat_value[u][v] > 0 and m < M:  # 도시 u에서 v로 갈 수 있고, 아직 경유할 도시가 있다면
                dp[v][m+1] = max(dp[v][m+1], dp[u][m] + eat_value[u][v])  # 도시 v에 도착했을 때의 기내식 점수를 업데이트한다.

print(max(dp[N]))  # N번 도시에 도착했을 때의 기내식 점수 중 최댓값을 출력한다.
